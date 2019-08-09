import json

from api.services.brazil_region_parser import get_abb_of
from api.services.string_services import normalize
from api.sources.cptec.getter.cptec_api_getter import CptecAPIGetter
from api.sources.cptec.getter.cptec_getter import CptecGetter
from api.sources.cptec.normalizer.cptec_normalizer import CptecNormalizer
from api.storage.source import Source


class CptecModel:

    def __init__(self, latitude=None, longitude=None):
        self.__today_data = None
        self.__week_data = None
        self.__latitude = latitude
        self.__longitude = longitude
        self.city = None
        self.state = None

    def make_request(self):
        self.__week_data = CptecAPIGetter(self.state, self.city).make_request()
        self.__today_data = CptecGetter(self.state, self.city).make_request()
        return self

    def make_site_request(self, region, city):
        self.__today_data = CptecGetter(get_abb_of(region), normalize(city).replace(' ', '-')).make_request()
        return self

    def make_api_request(self):
        self.__week_data = CptecAPIGetter(self.state, self.city).make_request()
        return self

    def get_today_resume(self):
        today_resume = CptecNormalizer(self.__today_data).get_resume()
        source = Source.objects().filter(source_name='CPTEC').first()

        return {
            'weatherCondition': self.__parse_weather_condition(source, today_resume['weather_condition']),
            'currentWeather': None,
            'maximumTemperature': today_resume['maximum_temperature'],
            'minimumTemperature': today_resume['minimum_temperature'],
            'rainProbability': today_resume['rain_probability'],
            'source': source.source_name,
            'sourceLogo': None,
            'link': json.loads(source.source_uri.to_json())
        }

    @staticmethod
    def __parse_weather_condition(source, weather_condition):
        for condition in source.conditions:
            for i in source.conditions[condition]:
                if i == weather_condition:
                    return condition
        return ''

    def get_week_resume(self):
        return CptecNormalizer(self.__week_data).get_week_resume()
