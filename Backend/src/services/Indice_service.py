from src.Entities.Grafico_chart_entity import Grafico_chart_entity
from  src.Entities.Indice_entity import Indice_entity
from  src.services.Base_service import Base_service


class Indice_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Indice_entity)
    def getIndiceOverview(self,idIndice: int,cnpj_empresa:str)-> dict[str, Grafico_chart_entity]:
        return self.repo.getIndiceOverview(idIndice,cnpj_empresa)


    

