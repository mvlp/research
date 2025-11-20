from datetime import date
from typing import Any
from src.infra.Database.Models.Indice import Indice
from  src.infra.Database.extensions import db
from src.Entities.Base_entity import Base_entity
class Indice_entity(Base_entity):
    id_grupo: int
    data_fim: date
    data_ini: date
    def to_model(self) -> Any:
        obj = Indice()
        obj.data_fim = self.data_fim 
        obj.data_ini = self.data_ini
        return obj

    
