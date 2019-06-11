from api.sources.cptec import CptecAPIGetter
from api.sources.cptec import CptecGetter
from api.sources.cptec import CptecNormalizer


class CptecModel:

    def __init__(self, country, state, city):
        self.country = country
        self.state = state
        self.city = city
        self.__today_data = None
        self.__week_data = None

    def make_request(self):
        self.__today_data = CptecGetter(self.state, self.city).make_request()
        self.__week_data = CptecAPIGetter(self.state, self.city).make_request()
        return self

    def get_today_resume(self):
        today_resume = CptecNormalizer(self.__today_data).get_resume()
        return {
            "weatherCondition": today_resume.weather_condition,
            "maximumTemperature": today_resume.maximum_temperature,
            "minimumTemperature": today_resume.minimum_temperature,
            "rainProbability": today_resume.rain_probability,
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
