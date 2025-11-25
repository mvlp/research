from typing import Any
from src.infra.Database.Models.pergunta import Pergunta
from src.Entities.Base_entity import Base_entity


class Pergunta_entity(Base_entity):
    texto: str
    def __init__(self, model) -> None:
        super().__init__(model)

    def to_model(self):
        p = Pergunta()
        p.id = self.id
        p.texto = self.texto
        return p
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "texto": self.texto,
        }

