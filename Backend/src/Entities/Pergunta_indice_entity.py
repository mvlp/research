from typing import Any
from src.infra.Database.Models.pergunta_indice import Pergunta_indice
from src.Entities.Base_entity import Base_entity

class Pergunta_indice_entity(Base_entity):
    id_indice = int
    id_pergunta = int

    def to_model(self) -> Any:
        obj = Pergunta_indice()
        obj.id_indice = self.id_indice
        obj.id_pergunta = self.id_pergunta
        return obj