from flask import request
from src.Entities.Governanca_entity import Governanca_entity
from src.infra.controller.BaseController import Base_controller
from src.services.Governanca_service import Governanca_service


class Governanca_controller(Base_controller):
    def __init__(self) -> None:
        self.service = Governanca_service()
        super().__init__(Governanca_service(), "governanca",Governanca_entity)

    def add_outras_rotas(self):
        @self.blueprint.get("grafico/quantidade/<str:capitulo>")
        def get_grafico_quantidade(capitulo: str):
            response = self.service.get_grafico_quantidade(capitulo)
            return self._convert_to_json(response)

        @self.blueprint.get("grafico/percentual/<str:capitulo>")
        def get_grafico_percentual(capitulo: str):
            response = self.service.get_grafico_percentual(capitulo)
            return self._convert_to_json(response)
        
