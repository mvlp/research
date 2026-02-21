from typing import Any

class Dataset:
  label:str
  data: list[float]
  def __init__(self,label:str) -> None:
    self.label = label
    self.data = []
  def to_dict(self) -> Any:
    return {
      "label": self.label,
      "data": self.data
    }



class Grafico_chart_entity:
  labels: list[str]
  datasets: list[Dataset]

  def __init__(self, labels: list[str], datasets: list[Dataset]):
    self.labels = labels
    self.datasets = datasets

  def to_dict(self) -> Any:
    data = []
    for d in self.datasets:
      data.append(d.to_dict())
    return {
        "labels": self.labels,
        "datasets": data
    }
    
