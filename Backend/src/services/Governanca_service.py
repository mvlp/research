from  src.Entities.Governanca_entity import Governanca_entity
from  src.services.Base_service import Base_service


class Governanca_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Governanca_entity)
        
    def get_grafico_percentual(self,capitulo:str):
        return self.get_grafico_percentual(capitulo)

    def get_grafico_quantidade(self,capitulo:str):
        return self.get_grafico_quantidade(capitulo)

    

