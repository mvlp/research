from Backend.src.Entities.pergunta_entity import Pergunta_entity
from Backend.src.services.Base_service import Base_service


class Pergunta_service(Base_service):
    def __init__(self, entity_cls: type) -> None:
        super().__init__(Pergunta_entity)


    

