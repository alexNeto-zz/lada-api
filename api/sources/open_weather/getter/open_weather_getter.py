import os

from api.sources.getter_definition import GetterDefinition


class OpenWeatherGetter(GetterDefinition):

    def __init__(self, latitude, longitude):
        config = {
            'url': 'https://api.openweathermap.org/data/2.5/forecast?lat={1}&lon={0}&units=metric&appid=' + self.__get_token(),
            'parser': 'json'
        }
        GetterDefinition.__init__(self, config, latitude, longitude)

    @classmethod
    def __get_token(cls):
        return os.environ.get("OPEN_WEATHER_TOKEN")
