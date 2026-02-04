from typing import Any
from  src.Entities.Dimensao_entity import Dimensao_entity, Pergunta_Dimensao_entity
from  src.services.Base_service import Base_service


class Dimensao_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Dimensao_entity)
    def create_one(self, entity: Any) -> Any:
        for index in range(len(entity.perguntas)):
            pergunta: Any = entity.perguntas[index]
            entity.perguntas[index] = Pergunta_Dimensao_entity(pergunta["id_pergunta"],pergunta["peso"])
        return super().create_one(entity)
    
    def update_one(self, entity: Dimensao_entity) -> Dimensao_entity | None:
        for index in range(len(entity.perguntas)):
            pergunta: Any = entity.perguntas[index]
            entity.perguntas[index] = Pergunta_Dimensao_entity(pergunta["id_pergunta"],pergunta["peso"])
        return super().update_one(entity)


    

