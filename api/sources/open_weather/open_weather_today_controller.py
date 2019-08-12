from flask_restful import Resource

from api.sources.open_weather.open_weather_model import OpenWeatherModel


class OpenWeatherTodayController(Resource):
    def __init__(self):
        self.__model = OpenWeatherModel()

    def get(self, latitude, longitude):
        return self.__model.get_today_resume(latitude, longitude)
