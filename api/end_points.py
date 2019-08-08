from flask_restful import Api

from api.source.source_controller import SourceController
from api.source.source_item_controller import SourceItemController


class EndPoints:

    def __init__(self, app):
        self.__api = Api(app)

    def add_resources(self):
        self.__api.add_resource(SourceController, '/source')
        self.__api.add_resource(SourceItemController, '/source/<source_name>')
