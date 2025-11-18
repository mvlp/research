
from Backend.src.infra.controller.BaseController import Base_controller
from Backend.src.services.Pergunta_indice_service import Pergunta_indice_service


class Pergunta_indice_controller(Base_controller):
    def __init__(self) -> None:
        super().__init__(Pergunta_indice_service(),"pergunta_indice")


