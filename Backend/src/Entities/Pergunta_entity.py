from src.infra.Database.Models.pergunta import Pergunta
from src.Entities.Base_entity import Base_entity


class Pergunta_entity(Base_entity):
    texto: str
    identificador: str
    def __init__(self, model) -> None:
        super().__init__(model)

    def to_model(self):
        p = Pergunta()
        p.id = self.id
        p.identificador = self.identificador
        p.texto = self.texto
        return p

