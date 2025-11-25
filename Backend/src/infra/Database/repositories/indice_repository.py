from typing import Any, Type

from sqlalchemy import Engine, select
from src.infra.Database.Models.Indice import Indice
from src.Entities.Indice_entity import Indice_entity
from src.infra.Database.Models.pergunta_indice import Pergunta_indice
from  src.infra.Database.repositories.Base_repository import E, M, BaseRepository
from sqlalchemy.orm import Session

class Indice_repository(BaseRepository):
    def __init__(self, engine: Engine):
        super().__init__(Indice_entity, Indice, engine)
    def create_one(self, entity: Indice_entity)-> Indice_entity:
        entity.id = None
        model = entity.to_model()
        with Session(self.sql_engine) as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            for id_pergunta in entity.perguntas:
                pergunta_indice = Pergunta_indice()
                pergunta_indice.id_indice = model.id
                pergunta_indice.id_pergunta = id_pergunta
                session.add(pergunta_indice)
            session.commit()
            session.refresh(model)
            entity = self.entity_class.from_model(model)
            perguntas_ids = (
                session.query(Pergunta_indice.id_pergunta)
                .filter(Pergunta_indice.id_indice == entity.id)
                .all()
            )
            entity.perguntas = [pid[0] for pid in perguntas_ids]

            return entity
        
    
    def get_all(self, filters: dict[str,Any] = {}) -> list[Indice_entity]:
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
                    session.query(Pergunta_indice.id_pergunta)
                    .filter(Pergunta_indice.id_indice == entity.id)
                    .all()
                )

                # .all() retorna lista de tuplas, então extrai valores
                entity.perguntas = [pid[0] for pid in perguntas_ids]
                lista.append(entity)

            return lista


    def get_one(self, id: int)-> Indice_entity | None:
        with Session(self.sql_engine) as session:
            pesquisa = select(self.model_class).where(self.model_class.id == id)
            result = session.execute(pesquisa).scalar_one_or_none()
            if not result:
                return None
            entity = self.entity_class.from_model(result)
            perguntas_ids = (
                session.query(Pergunta_indice.id_pergunta)
                .filter(Pergunta_indice.id_indice == entity.id)
                .all()
            )

            # .all() retorna lista de tuplas, então extrai valores
            entity.perguntas = [pid[0] for pid in perguntas_ids]

            return entity
        
    def update_one(self, entity: Indice_entity) -> Indice_entity | None:
        with Session(self.sql_engine) as session:
            obj = session.get(self.model_class, entity.id)
            if not obj:
                return None
            for key, value in vars(entity).items():
                if key == "id":
                    continue
                setattr(obj, key, value)
            # Remove todas as perguntas antigas
            session.query(Pergunta_indice).filter_by(id_indice=entity.id).delete()
            ##Readiciona tudo novamente
            for id_pergunta in entity.perguntas:
                pergunta_indice = Pergunta_indice()
                pergunta_indice.id_indice = entity.id
                pergunta_indice.id_pergunta = id_pergunta
                session.add(pergunta_indice)
                session.commit()


            session.commit()
            session.refresh(obj)
            entity = self.entity_class.from_model(obj)




            return entity
