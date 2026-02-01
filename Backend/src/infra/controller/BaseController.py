import json
from typing import Generic,Any, Type

from flask import Blueprint, jsonify, request
from sqlalchemy import inspect

from  src.infra.Database.repositories.Base_repository import E, M
from  src.services.Base_service import Base_service
class Base_controller(Generic[E]):
    def __init__(self , service: Base_service, name: str,entity_class: type[E]) -> None:
        self.service = service
        self.name = name
        self.blueprint = Blueprint(name,"Controller_" + name)
        self.entity_class = entity_class
        self.add_basic_routes_to_blueprint()
    def add_basic_routes_to_blueprint(self):
        @self.blueprint.get("")
        def get_all():
            params = request.args
            response = self.service.get_all(params)
            return self._convert_to_json(response)
        @self.blueprint.get("getOne")
        def get_one():
            id: Any = request.args.get('id')
            response = self.service.get_one(id)
            return self._convert_to_json(response)
        @self.blueprint.put("")
        def update_one():
            data = request.get_json()
            entity = self.entity_class(data)
            response = self.service.update_one(entity)
            return self._convert_to_json(response)
        @self.blueprint.post("")
        def create_one():
            data = request.get_json()
            entity = self.entity_class(data)
            response = self.service.create_one(entity)
            return self._convert_to_json(response)
        @self.blueprint.delete("<int:id>")
        def delete_one(id: int):
            response = self.service.delete_one(id)
            return self._convert_to_json(response)

    def _convert_to_json(self,obj:Any):
        if obj == None: return jsonify(obj)
        elif isinstance(obj,dict):
            return jsonify({
                k: self._convert_to_json(v).json
                if hasattr(self._convert_to_json(v), "json")
                else v
                for k, v in obj.items()
            })
        elif isinstance(obj,list):
            lista = []
            for item in obj: 
                lista.append(item.to_dict())
            return jsonify(lista)
        else: return jsonify(obj.to_dict())