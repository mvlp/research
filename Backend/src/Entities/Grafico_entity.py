class Grafico_entity:
  nome: str
  labels: list[str]
  Limite_superior: list[float] | None
  Limite_inferior: list[float] | None
  Dado: list[float]
  def __init__(self, nome:str, labels: list[str], dado: list[float], limite_superior: list[float] | None, limite_inferior: list[float] | None):
    self.labels = labels
    self.Limite_superior = limite_superior
    self.Limite_inferior = limite_inferior
    self.Dado = dado

  