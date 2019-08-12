import datetime

from api.services.weather_validator import temperature, rain_probability
from api.sources.open_weather.getter.open_weather_getter import OpenWeatherGetter


class OpenWeatherNormalizer:

    def get_resume(self, latitude, longitude):
        result = OpenWeatherGetter(latitude, longitude).make_request()
        today = self.__filter_today_forecast(result['list'])
        return {
            "weather_condition": today[0]['weather'][0]['id'],
            "current_weather": temperature(today[0]['main']['temp']),
            "maximum_temperature": temperature(self.__get_max(today)),
            "minimum_temperature": temperature(self.__get_min(today)),
            "sun_rise": None,
            "sun_down": None,
            "rain_probability": rain_probability(self.__get_rain_probability(today))
        }

    def __get_rain_probability(self, today):
        result_list = []
        for i in today:
            result_list.append(self.__get_item_rain_probability(i))
        return max(result_list)

    @classmethod
    def __get_item_rain_probability(cls, today):
        try:
            return today['rain']
        except KeyError:
            return 0

    def __filter_today_forecast(self, forecast_list):
        result_list = []
        for i in forecast_list:
            if self.__compare_date(i['dt_txt'].split(" ")[0]):
                result_list.append(i)
        return result_list

    @classmethod
    def __compare_date(cls, date):
        return date == datetime.datetime.now().date().isoformat()

    @classmethod
    def __get_min(cls, forecast_list):
        min_list = []
        for i in forecast_list:
            min_list.append(i['main']['temp_min'])
        return min(min_list)

    @classmethod
    def __get_max(cls, forecast_list):
        min_list = []
        for i in forecast_list:
            min_list.append(i['main']['temp_max'])
        return max(min_list)
