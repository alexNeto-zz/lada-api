from flask_restful import Api

from api.about.about_controller import AboutController
from api.source.source_controller import SourceController
from api.source.source_item_controller import SourceItemController
from api.source_for_location.source_for_location_controller import SourceForLocationController
from api.sources.cptec.cptec_today_controller import CPTECTodayController
from api.sources.open_weather.open_weather_today_controller import OpenWeatherTodayController
from api.vote.vote_controller import VoteController


class EndPoints:

    def __init__(self, app):
        self.__api = Api(app)

    def add_resources(self):
        # GENERAL
        self.__api.add_resource(AboutController, '/about')
        # SOURCE
        self.__api.add_resource(SourceController, '/source')
        self.__api.add_resource(SourceItemController, '/source/<source_name>')
        self.__api.add_resource(SourceForLocationController, '/source/list-available/<country>')
        # VOTES
        self.__api.add_resource(VoteController, '/vote_of/<location>/source/<string:source>')
        # CPTEC
        self.__api.add_resource(CPTECTodayController, '/CPTEC/INPE/today/<region>/<city>')
        # OPEN WEATHER
        self.__api.add_resource(OpenWeatherTodayController, '/Open Weather/today/<latitude>/<longitude>')
