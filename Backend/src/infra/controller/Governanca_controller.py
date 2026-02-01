from flask import jsonify, request
from src.Entities.Governanca_entity import Governanca_entity
from src.infra.controller.BaseController import Base_controller
from src.services.Governanca_service import Governanca_service


class Governanca_controller(Base_controller):
    def __init__(self) -> None:
        self.service = Governanca_service()
        super().__init__(Governanca_service(), "governanca",Governanca_entity)
        self.add_outras_rotas()

    def add_outras_rotas(self):

        @self.blueprint.get("empresa")
        def get_empresa():
            empresa = request.args.get('empresa')
            if not empresa: return jsonify({"Erro": "Parâmetros não informados"})
            response = self.service.get_empresa(empresa)
            return self._convert_to_json(response)
        
        @self.blueprint.get("faltantes")
        def get_dados_faltantes():
            response = self.service.get_dados_faltantes()
            return self._convert_to_json(response)


        @self.blueprint.get("tabela")
        def get_tabela_percentuais():
            response = self.service.get_tabela_percentuais()
            return self._convert_to_json(response)

        @self.blueprint.get("grafico/quantidade")
        def get_grafico_quantidade():
            capitulo = request.args.get('capitulo')
            resposta = request.args.get('resposta')
            if not capitulo or not resposta: return jsonify({"Erro": "Parâmetros não informados"})
            response = self.service.get_grafico_quantidade(capitulo,resposta)
            return self._convert_to_json(response)

        @self.blueprint.get("grafico/percentual")
        def get_grafico_percentual():
            capitulo = request.args.get('capitulo')
            resposta = request.args.get('resposta')
            if not capitulo or not resposta: return jsonify({"Erro": "Parâmetros não informados"})
            response = self.service.get_grafico_percentual(capitulo,resposta)
            return self._convert_to_json(response)
        
