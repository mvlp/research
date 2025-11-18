from  src.infra.controller.BaseController import Base_controller
from  src.services.Indice_grupo_service import Indice_grupo_service
from  src.services.Indice_service import Indice_service


class Indice_grupo_controller(Base_controller):
    def __init__(self) -> None:
        super().__init__(Indice_grupo_service(),"indice_grupo")


    

