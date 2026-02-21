from typing import Any
from src.infra.Database.Models.auto.cgvn_praticas import cgvn_praticas
from src.Entities.Base_entity import Base_entity
from src.infra.Database.extensions import db
from datetime import date

class Governanca_entity(Base_entity):
    CNPJ_Companhia: str
    Data_Referencia: date
    Nome_Empresarial: str
    ID_Documento: str
    ID_Item: str
    Capitulo: str
    Principio: str
    Pratica_Recomendada: str 
    Pratica_Adotada: str
    Explicacao: str
    Data_Entrega: date 
    gc_factor: str
    gc_value: int
    
    def to_model(self) -> Any:
        obj = cgvn_praticas()
        obj.CNPJ_Companhia = self.CNPJ_Companhia
        obj.Data_Referencia = self.Data_Referencia
        obj.Nome_Empresarial = self.Nome_Empresarial
        obj.ID_Documento = self.ID_Documento
        obj.ID_Item = self.ID_Item
        obj.Capitulo = self.Capitulo
        obj.Principio = self.Principio
        obj.Pratica_Recomendada = self.Pratica_Recomendada 
        obj.Pratica_Adotada = self.Pratica_Adotada
        obj.Explicacao = self.Explicacao
        obj.Data_Entrega = self.Data_Entrega 
        obj.gc_factor = self.gc_factor
        obj.gc_value = self.gc_value
        return obj
    
    def to_dict(self) -> Any:
        return {
            "CNPJ_Companhia": self.CNPJ_Companhia, 
            "Data_Entrega": self.Data_Entrega, 
            "Data_Referencia": self.Data_Referencia, 
            "Nome_Empresarial": self.Nome_Empresarial, 
        }
    