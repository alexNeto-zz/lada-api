import json

from flask_restful import Resource

from api.source_for_location.source_for_location_model import SourceForLocationModel


class SourceForLocationController(Resource):

    def __init__(self):
        self.__model = SourceForLocationModel()

    def get(self, country):
        return json.loads(self.__model.get_for_location(country).to_json())
