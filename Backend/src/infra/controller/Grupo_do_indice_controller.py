from src.Entities.Grupo_do_indice_entity import Grupo_do_indice_entity
from  src.infra.controller.BaseController import Base_controller
from  src.services.Grupo_do_indice_service import Grupo_do_indice_service


class Grupo_do_indice_controller(Base_controller):
    def __init__(self) -> None:
        super().__init__(Grupo_do_indice_service(),"Grupo_do_indice",Grupo_do_indice_entity)


    

