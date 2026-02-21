from   src.Entities.Pergunta_entity import Pergunta_entity
from  src.services.Base_service import Base_service


class Pergunta_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Pergunta_entity)


    

