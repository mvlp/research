from abc import ABC, abstractmethod
from typing import Any

class Base_entity:
    id: Any
    def __init__(self, data: dict,):
        self.id = None
        for key, value in data.items():
            setattr(self, key, value)

    @abstractmethod
    def to_model(self)-> Any:
        pass

    @abstractmethod
    def to_dict(self)-> Any:
        pass
    
    @classmethod
    def from_model(cls, model): 
        model_dict: dict = model.__dict__
        model_dict.pop("_sa_instance_state")
        obj = cls(model_dict)
        return obj