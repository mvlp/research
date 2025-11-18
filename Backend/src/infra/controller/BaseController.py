import json
from typing import Generic,Any

from flask import Blueprint, jsonify, request

from  src.infra.Database.repositories.Base_repository import E, M
from  src.services.Base_service import Base_service
class Base_controller(Generic[E]):
    def __init__(self, service: Base_service, name: str) -> None:
        self.service = service
        self.name = name
        self.blueprint = Blueprint(name,"Controller_" + name)
        self.add_basic_routes_to_blueprint()
    def add_basic_routes_to_blueprint(self):
        @self.blueprint.get("<int:id>")
        def get_one(self, id: int):
            response = self.service.get_one(id)
            return self._convert_to_json(response)
        @self.blueprint.put("")
        def update_one(self):
            entity = request.form
            response = self.service.update_one(entity)
            return self._convert_to_json(response)
        @self.blueprint.post("")
        def create_one(self):
            entity = request.form
            response = self.service.create_one(entity)
            return self._convert_to_json(response)
        @self.blueprint.delete("<int:id>")
        def delete_one(self, id: int):
            response = self.service.delete_one(id)
            return self._convert_to_json(response)

    def _convert_to_json(self,variable:Any):
        return jsonify(variable)