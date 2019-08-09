from api.services.weather_validator import rain_probability, temperature
from api.sources.cptec.scrapy.cptec_api_scrapy import CptecAPIScrapy
from api.sources.cptec.scrapy.cptec_scrapy import CptecScrapy


class CptecNormalizer:

    def __init__(self, today_data=None, week_data=None):
        self.__scrapy = CptecScrapy(today_data) if today_data else CptecAPIScrapy(week_data)

    def get_resume(self):
        return {
            "weather_condition": self.__scrapy.get_weather_condition(),
            "maximum_temperature": temperature(self.__scrapy.get_maximum_temperature()),
            "minimum_temperature": temperature(self.__scrapy.get_minimum_temperature()),
            "sun_rise": self.__scrapy.get_sun_rise(),
            "sun_down": self.__scrapy.get_sun_down(),
            "rain_probability": rain_probability(self.__scrapy.get_rain_probability().replace('%', ''))
        }

    def get_week_resume(self):
        return {
            "updated_at": self.__scrapy.get_updated_at(),
            "weather": self.__scrapy.get_week_resume()

        }
