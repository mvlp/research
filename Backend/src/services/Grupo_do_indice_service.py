from src.Entities.Grupo_do_indice_entity import Grupo_do_indice_entity
from src.infra.Database.Models.Grupo_do_indice import Grupo_do_indice
from  src.Entities.Indice_entity import Indice_entity
from  src.services.Base_service import Base_service


class Grupo_do_indice_service(Base_service):
    def __init__(self) -> None:
        super().__init__(Grupo_do_indice_entity)


    

