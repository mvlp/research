from  src.Entities.Indice_entity import Indice_entity
from  src.services.Base_service import Base_service


class Indice_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Indice_entity)


    

