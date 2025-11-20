from abc import ABC, abstractmethod
from typing import Any

class Base_entity:
    id: int | None
    def __init__(self, data: dict,):
        self.id = None
        for key, value in data.items():
            setattr(self, key, value)

    @abstractmethod
    def to_model(self)-> Any:
        pass
    
    @classmethod
    def from_model(cls, model): 
        obj = cls(model)
        return obj