from Backend.src.Entities.pergunta_indice_entity import Pergunta_indice_entity
from Backend.src.services.Base_service import Base_service


class Pergunta_indice_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Pergunta_indice_entity)


    

