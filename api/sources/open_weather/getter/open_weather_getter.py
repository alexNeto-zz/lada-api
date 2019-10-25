import os

from api.sources.getter_definition import GetterDefinition


def get_token():
    return os.environ.get("OPEN_WEATHER_TOKEN")


class OpenWeatherGetter(GetterDefinition):

    def __init__(self, service, latitude, longitude):
        config = {
            'url': 'https://api.openweathermap.org/data/2.5/' +
                   service + '?lat={0}&lon={1}&units=metric&appid=' + get_token(),
            'parser': 'json'
        }
        GetterDefinition.__init__(self, config, longitude, latitude)
