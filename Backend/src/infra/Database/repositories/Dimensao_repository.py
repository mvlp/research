from typing import Any, Type

from sqlalchemy import Engine, select
from src.infra.Database.Models.Dimensao import Dimensao
from src.Entities.Dimensao_entity import Dimensao_entity
from src.infra.Database.Models.pergunta_dimensao import Pergunta_Dimensao
from  src.infra.Database.repositories.Base_repository import E, M, BaseRepository
from sqlalchemy.orm import Session

class Dimensao_repository(BaseRepository):
    def __init__(self, engine: Engine):
        super().__init__(Dimensao_entity, Dimensao, engine)
    def create_one(self, entity: Dimensao_entity)-> Dimensao_entity:
        entity.id = None
        model = entity.to_model()
        with Session(self.sql_engine) as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            for id_pergunta in entity.perguntas:
                pergunta_Dimensao = Pergunta_Dimensao()
                pergunta_Dimensao.id_Dimensao = model.id
                pergunta_Dimensao.id_pergunta = id_pergunta
                session.add(pergunta_Dimensao)
            session.commit()
            session.refresh(model)
            entity = self.entity_class.from_model(model)
            perguntas_ids = (
                session.query(Pergunta_Dimensao.id_pergunta)
                .filter(Pergunta_Dimensao.id_Dimensao == entity.id)
                .all()
            )
            entity.perguntas = [pid[0] for pid in perguntas_ids]

            return entity
        
    
    def get_all(self, filters: dict[str,Any] = {}) -> list[Dimensao_entity]:
        with Session(self.sql_engine) as session:
            query = select(self.model_class)
            for key, value in filters.items():
                query = query.where(getattr(self.model_class, key) == value)
            results = session.execute(query).scalars().all()

            lista = []

            for model in results:
                entity = self.entity_class.from_model(model)
                # Carregar IDs das perguntas deste índice
                perguntas_ids = (
                    session.query(Pergunta_Dimensao.id_pergunta)
                    .filter(Pergunta_Dimensao.id_Dimensao == entity.id)
                    .all()
                )

                # .all() retorna lista de tuplas, então extrai valores
                entity.perguntas = [pid[0] for pid in perguntas_ids]
                lista.append(entity)

            return lista


    def get_one(self, id: int)-> Dimensao_entity | None:
        with Session(self.sql_engine) as session:
            pesquisa = select(self.model_class).where(self.model_class.id == id)
            result = session.execute(pesquisa).scalar_one_or_none()
            if not result:
                return None
            entity = self.entity_class.from_model(result)
            perguntas_ids = (
                session.query(Pergunta_Dimensao.id_pergunta)
                .filter(Pergunta_Dimensao.id_Dimensao == entity.id)
                .all()
            )

            # .all() retorna lista de tuplas, então extrai valores
            entity.perguntas = [pid[0] for pid in perguntas_ids]

            return entity
        
    def update_one(self, entity: Dimensao_entity) -> Dimensao_entity | None:
        with Session(self.sql_engine) as session:
            obj = session.get(self.model_class, entity.id)
            if not obj:
                return None
            for key, value in vars(entity).items():
                if key == "id":
                    continue
                setattr(obj, key, value)
            # Remove todas as perguntas antigas
            session.query(Pergunta_Dimensao).filter_by(id_Dimensao=entity.id).delete()
            ##Readiciona tudo novamente
            for id_pergunta in entity.perguntas:
                pergunta_Dimensao = Pergunta_Dimensao()
                pergunta_Dimensao.id_Dimensao = entity.id
                pergunta_Dimensao.id_pergunta = id_pergunta
                session.add(pergunta_Dimensao)
                session.commit()


            session.commit()
            session.refresh(obj)
            entity = self.entity_class.from_model(obj)




            return entity
