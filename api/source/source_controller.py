import json
from typing import List

from flask_restful import Resource

from api.source.source_model import SourceModel
from api.storage.source import Source


class SourceController(Resource):

    def __init__(self):
        self.__model = SourceModel()

    def get(self) -> List[Source]:
        return json.loads(self.__model.get_source_list().to_json())
