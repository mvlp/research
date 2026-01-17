from typing import Any


class Grafico_entity:
  nome: str
  labels: list[str]
  Limite_superior: list[float]
  Limite_inferior: list[float]
  Dado: list[float]
  def __init__(self, nome:str, labels: list[str], dado: list[float], limite_superior: list[float], limite_inferior: list[float]):
    self.nome = nome
    self.labels = labels
    self.Limite_superior = limite_superior
    self.Limite_inferior = limite_inferior
    self.Dado = dado

  def to_dict(self) -> Any:
    return {
        "Nome": self.nome,
        "Labels": self.labels,
        "Limite_superior": self.Limite_superior,
        "Limite_inferior": self.Limite_inferior,
        "Dado": self.Dado
    }
    
