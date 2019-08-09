from flask_restful import Api

from api.source.source_controller import SourceController
from api.source.source_item_controller import SourceItemController
from api.source_for_location.source_for_location_controller import SourceForLocationController
from api.sources.cptec.cptec_today_controller import CPTECTodayController


class EndPoints:

    def __init__(self, app):
        self.__api = Api(app)

    def add_resources(self):
        # SOURCE
        self.__api.add_resource(SourceController, '/source')
        self.__api.add_resource(SourceItemController, '/source/<source_name>')
        self.__api.add_resource(SourceForLocationController, '/source/list-available/<country>')
        # CPTEC
        self.__api.add_resource(CPTECTodayController, '/cptec/today/<region>/<city>')
