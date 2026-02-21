from datetime import date
from typing import Any
from src.infra.Database.Models.Dimensao import Dimensao
from  src.infra.Database.extensions import db
from src.Entities.Base_entity import Base_entity
class Pergunta_Dimensao_entity:
    id_pergunta: int
    peso: float
    def __init__(self,id_pergunta:int,peso:float) -> None:
        self.id_pergunta = id_pergunta
        self.peso = peso
    def to_dict(self):
        return {
            "id_pergunta": self.id_pergunta,
            "peso": self.peso
        }

class Dimensao_entity(Base_entity):
    idIndice: int
    sigla: str
    perguntas: list[Pergunta_Dimensao_entity]

    def to_model(self) -> Any:
        obj = Dimensao()
        obj.idIndice = self.idIndice 
        obj.sigla = self.sigla
        return obj

    def to_dict(self) -> Any:
        return {
            "id": self.id,
            "sigla": self.sigla,
            "perguntas": [p.to_dict() for p in self.perguntas],
            "idIndice": self.idIndice, 
        }