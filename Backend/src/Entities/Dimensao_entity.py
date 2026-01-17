from datetime import date
from typing import Any
from src.infra.Database.Models.Dimensao import Dimensao
from  src.infra.Database.extensions import db
from src.Entities.Base_entity import Base_entity
class Dimensao_entity(Base_entity):
    idIndice: int
    perguntas: list[int]

    def to_model(self) -> Any:
        obj = Dimensao()
        obj.idIndice = self.idIndice 
        return obj

    def to_dict(self) -> Any:
        return {
            "id": self.id,
            "perguntas": self.perguntas,
            "idIndice": self.idIndice, 
        }
    
