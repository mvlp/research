from Backend.src.Entities.Indice_grupo_entity import Indice_grupo_entity
from Backend.src.services.Base_service import Base_service


class Indice_grupo_service(Base_service):
    def __init__(self, entity_cls: type) -> None:
        super().__init__(Indice_grupo_entity)


    

