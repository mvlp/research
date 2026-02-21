from flask import jsonify, request
from src.Entities.Cotacao_b3_entity import Cotacao_b3_entity
from src.services.Cotacao_b3_service import Cotacao_b3_service
from src.Entities.Dimensao_entity import Dimensao_entity
from  src.infra.controller.BaseController import Base_controller
from  src.services.Dimensao_service import Dimensao_service


class Cotacao_b3_controller(Base_controller):
    def __init__(self) -> None:
        self.service = Cotacao_b3_service()
        super().__init__(Cotacao_b3_service(),"cotacao_b3",Cotacao_b3_entity)
        self.add_outras_rotas()

    def add_outras_rotas(self):
        @self.blueprint.get("corrigido")
        def getCorrigido():
            isin = request.args.get('isin')
            codigo = request.args.get('codigo')

            if not isin or not codigo: return jsonify({"Erro": "Parâmetros não informados"})
            res = self.service.getCorrigido(isin,codigo)
            return self._convert_to_json(res)