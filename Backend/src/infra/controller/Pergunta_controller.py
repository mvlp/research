
from src.Entities.Pergunta_entity import Pergunta_entity
from  src.infra.controller.BaseController import Base_controller
from  src.services.Pergunta_service import Pergunta_service


class Pergunta_controller(Base_controller):
    def __init__(self) -> None:
        super().__init__(Pergunta_service(),"pergunta",Pergunta_entity)


