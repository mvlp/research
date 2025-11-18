from  src.Entities.Indice_grupo_entity import Indice_grupo_entity
from  src.services.Base_service import Base_service


class Indice_grupo_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Indice_grupo_entity)


    

