import json

from flask import request
from flask_restful import Resource

from api.source.source_model import SourceModel


class SourceItemController(Resource):

    def __init__(self):
        self.__model = SourceModel()

    def get(self, source_name: str):
        return json.loads(self.__model.get_by_source_name(source_name).to_json())

    def post(self, _):
        return json.loads(self.__model.new_source(**request.get_json()).to_json())
