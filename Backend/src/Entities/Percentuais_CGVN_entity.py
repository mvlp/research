from typing import Any


class Percentuais_CGVN_Entity:
  item: str
  principio: str
  pratica_recomendada: str
  perc_nao: float
  perc_nao_aplica: float
  perc_parcialmente: float
  perc_sim: float
  def __init__(self, item: str,principio: str,pratica_recomendada: str,perc_nao: float,perc_nao_aplica: float,perc_parcialmente: float,perc_sim: float):
    self.item = item
    self.principio = principio
    self.pratica_recomendada = pratica_recomendada
    self.perc_nao = perc_nao
    self.perc_nao_aplica = perc_nao_aplica
    self.perc_parcialmente = perc_parcialmente
    self.perc_sim = perc_sim

  def to_dict(self) -> Any:
    return {
        "item": self.item,
        "principio": self.principio,
        "pratica_recomendada": self.pratica_recomendada,
        "perc_nao": self.perc_nao,
        "perc_nao_aplica": self.perc_nao_aplica,
        "perc_parcialmente": self.perc_parcialmente,
        "perc_sim": self.perc_sim
    }
    
