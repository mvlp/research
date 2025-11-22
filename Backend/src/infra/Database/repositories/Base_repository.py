from sqlalchemy import Engine, select, delete, update
from sqlalchemy.orm import Session
from typing import TypeVar, Generic, Type
from src.infra.Database.Models.Base_model import Base_model
from src.Entities.Base_entity import Base_entity
E = TypeVar("E",bound=Base_entity) ## define uma entidade abstrata que será passado na inicialização da classe
M = TypeVar("M",bound=Base_model) ## define um model abstrato que será passado na inicialização da classe

### A grande vantagem de termos essa camada separa é por que permite que todo a complexidade do banco de dados fique completamente
### isolada do restante da aplicação, portanto, nenhum problema que acontecer no app, será culpa do bd e vice versa
class BaseRepository(Generic[E,M]):
    def __init__(self, entity_class: Type[E], model_class: Type[M], engine:Engine):
        self.entity_class = entity_class
        self.model_class = model_class
        self.sql_engine = engine

    def get_all(self) -> list[E]:
        with Session(self.sql_engine) as session:
            query = select(self.model_class)
            results = session.execute(query).scalars().all()
            lista = []
            for r in results:
                lista.append(self.entity_class.from_model(r))
            return lista

    def create_one(self, entity: E)-> E:
        entity.id = None
        model = entity.to_model()
        with Session(self.sql_engine) as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return self.entity_class.from_model(model)

    def get_one(self, id: int)-> E | None:
        with Session(self.sql_engine) as session:
            pesquisa = select(self.model_class).where(self.model_class.id == id)
            result = session.execute(pesquisa).scalar_one_or_none()
            if not result:
                return None
            entity = self.entity_class.from_model(result)
            return entity
        
    def delete_one(self, id: int):
        with Session(self.sql_engine) as session:
            pesquisa = delete(self.model_class).where(self.model_class.id == id)
            result = session.execute(pesquisa)
            session.commit()
            return None

    def update_one(self, entity: E) -> E | None:
        with Session(self.sql_engine) as session:
            obj = session.get(self.model_class, entity.id)
            if not obj:
                return None
            for key, value in vars(entity).items():
                if key == "id":
                    continue
                setattr(obj, key, value)

            session.commit()
            session.refresh(obj)
            entity = self.entity_class.from_model(obj)
            return entity
        


