from src.infra.Database.repositories.governanca_repository import Governanca_repository
from  src.Entities.Governanca_entity import Governanca_entity
from  src.services.Base_service import Base_service


class Governanca_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Governanca_entity)

    def get_empresa(self,empresa:str):
        return self.repo.get_empresa(empresa)
    
    def get_dados_faltantes(self):
        return self.repo.get_dados_faltantes()

    def get_tabela_percentuais(self):
        return self.repo.get_tabela_percentuais()
    def get_grafico_percentual(self,capitulo:str,resposta:str):
        return self.repo.get_grafico_percentual(capitulo, resposta)

    def get_grafico_quantidade(self,capitulo:str,resposta:str):
        return self.repo.get_grafico_quantidade(capitulo, resposta)

    

