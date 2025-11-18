from Backend.src.Entities.Governanca_entity import Governanca_entity
from Backend.src.services.Base_service import Base_service


class Governanca_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Governanca_entity)


    

