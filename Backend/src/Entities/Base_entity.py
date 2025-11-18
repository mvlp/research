from abc import ABC, abstractmethod
from typing import Any

class Base_entity:
    id: int

    def __init__(self, model) -> None:
        self = model
    
    def to_model(self) -> Any:
        return self