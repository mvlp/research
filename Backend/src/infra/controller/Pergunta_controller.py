
from Backend.src.infra.controller.BaseController import Base_controller
from Backend.src.services.Pergunta_service import Pergunta_service


class Pergunta_controller(Base_controller):
    def __init__(self) -> None:
        super().__init__(Pergunta_service(),"pergunta")


