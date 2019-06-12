from api.sources.cptec.getter.cptec_api_getter import CptecAPIGetter
from api.sources.cptec.getter.cptec_getter import CptecGetter
from api.sources.cptec.normalizer.cptec_normalizer import CptecNormalizer
from api.sources.cptec.scrapy.cptec_api_scrapy import CptecAPIScrapy


class CptecModel:

    def __init__(self, x, y):
        self.__today_data = None
        self.__week_data = None
        self.__x = x
        self.__y = y
        self.city = None
        self.state = None
        self.__get_location()

    def make_request(self):
        self.__week_data = CptecAPIGetter(self.state, self.city).make_request()
        self.__today_data = CptecGetter(self.state, self.city).make_request()
        return self

    def __get_location(self):
        data = CptecAPIScrapy(CptecAPIGetter(self.__x, self.__y).make_request())
        self.city = data.get_city()
        self.state = data.get_state()

    def get_today_resume(self):
        today_resume = CptecNormalizer(self.__today_data).get_resume()
        return {
            "weatherCondition": today_resume['weather_condition'],
            "maximumTemperature": today_resume['maximum_temperature'],
            "minimumTemperature": today_resume['minimum_temperature'],
            "rainProbability": today_resume['rain_probability'],
            "source": "",
            "sourceLogo": "",
            "link": "",
        }

    def get_today_complete(self):
        pass

    def get_week_resume(self):
        return CptecNormalizer(self.__week_data).get_week_resume()

    def get_week_complete(self):
        pass
