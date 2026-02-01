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
    datasets = []
    if (len(self.Limite_superior)): datasets.append(
          {
            "label":"Limite superior",
            "data": self.Limite_superior,
            "backgroundColor": "rgba(100,116,139,0.4)",
            "pointRadius": 0,
            "borderWidth": 0,
            "fill": 2,
            "order": 2

          }
    )
      
    if (len(self.Dado)): datasets.append(
          {
            "label":"Dados",
            "data": self.Dado,
            "backgroundColor": "rgb(85, 190, 122)",
            "borderColor": "rgb(85, 190, 122)",
            "order": 1
          }
    )
    if (len(self.Limite_inferior)): datasets.append(
          {
            "label":"Limite inferior",
            "data": self.Limite_inferior,
            "backgroundColor": "rgba(100,116,139,0.35)",
            "pointRadius": 0,
            "borderWidth": 0,
            "order": 2,

          }
    )
    return {
        "Nome": self.nome,
        "labels": self.labels,
        "datasets": datasets
    }
    
