from datetime import date
from typing import Any
from src.infra.Database.Models.Indice import Indice
from  src.infra.Database.extensions import db
from src.Entities.Base_entity import Base_entity
class Indice_entity(Base_entity):
    idGrupo: int
    perguntas: list[int]

    def to_model(self) -> Any:
        obj = Indice()
        obj.idGrupo = self.idGrupo 
        return obj

    def to_dict(self) -> Any:
        return {
            "id": self.id,
            "perguntas": self.perguntas,
            "idGrupo": self.idGrupo, 
        }
    
