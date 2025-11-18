from src.Entities.Governanca_entity import Governanca_entity
from src.infra.controller.BaseController import Base_controller
from src.services.Governanca_service import Governanca_service


class Governanca_controller(Base_controller):
    def __init__(self) -> None:
        super().__init__(Governanca_service(), "governanca")


    

