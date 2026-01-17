from  src.Entities.Dimensao_entity import Dimensao_entity
from  src.services.Base_service import Base_service


class Dimensao_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Dimensao_entity)


    

