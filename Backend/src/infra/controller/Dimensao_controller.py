from src.Entities.Dimensao_entity import Dimensao_entity
from  src.infra.controller.BaseController import Base_controller
from  src.services.Dimensao_service import Dimensao_service


class Dimensao_controller(Base_controller):
    def __init__(self) -> None:
        super().__init__(Dimensao_service(),"Dimensao",Dimensao_entity)


    

