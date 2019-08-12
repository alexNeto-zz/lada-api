import json

from api.sources.open_weather.normalizer.open_weather_normalizer import OpenWeatherNormalizer
from api.storage.source import Source


class OpenWeatherModel:

    @classmethod
    def get_today_resume(cls, latitude, longitude):
        today_resume = OpenWeatherNormalizer().get_resume(latitude, longitude)
        source = Source.objects().filter(source_name='Open Weather').first()
        return {
            'weatherCondition': '',
            'currentWeather': today_resume['current_weather'],
            'maximumTemperature': today_resume['maximum_temperature'],
            'minimumTemperature': today_resume['minimum_temperature'],
            'rainProbability': today_resume['rain_probability'],
            'source': source.source_name,
            'sourceLogo': None,
            'link': json.loads(source.source_uri.to_json())
        }
