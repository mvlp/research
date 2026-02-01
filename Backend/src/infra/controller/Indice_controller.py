from flask import jsonify, request
from src.Entities.Indice_entity import Indice_entity
from  src.infra.controller.BaseController import Base_controller
from  src.services.Indice_service import Indice_service


class Indice_controller(Base_controller):
    def __init__(self) -> None:
        self.service = Indice_service()
        super().__init__(Indice_service(),"Indice",Indice_entity)
        self.add_outras_rotas()
        
    def add_outras_rotas(self):
        @self.blueprint.get("overview")
        def getIndiceOverview():
            idIndice = request.args.get('idIndice')
            cnpj_empresa = request.args.get('cnpj_empresa')
            if not idIndice or not cnpj_empresa: return jsonify({"Erro": "Parâmetros não informados"})
            res = self.service.getIndiceOverview(int(idIndice),cnpj_empresa)
            return self._convert_to_json(res)



    

