from datetime import date
from typing import Any
from src.infra.Database.Models.Indice import Indice
from src.infra.Database.Models.Dimensao import Dimensao
from src.infra.Database.extensions import db
from src.Entities.Base_entity import Base_entity
class Indice_entity(Base_entity):
    data_fim: date
    data_ini: date
    nome: str
    def to_model(self) -> Any:
        obj = Indice()
        obj.nome = self.nome
        obj.data_fim = self.data_fim 
        obj.data_ini = self.data_ini
        return obj

    def to_dict(self) -> Any:
        return {
            "id": self.id,
            "data_fim": self.data_fim,
            "data_ini": self.data_ini,
            "nome": self.nome, 
        }
    
