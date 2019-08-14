import datetime

from api.services.weather_validator import temperature, rain_probability
from api.sources.open_weather.getter.open_weather_getter import OpenWeatherGetter


class OpenWeatherNormalizer:

    def get_resume(self, latitude, longitude):
        three_hour_result = OpenWeatherGetter('forecast', latitude, longitude).make_request()
        today = self.__filter_today_forecast(three_hour_result['list'])
        try:
            if len(today) > 0:
                return self.__get_hourly_model(today)
            else:
                current_result = OpenWeatherGetter('weather', latitude, longitude).make_request()
                return self.__get_current_model(current_result)
        except IndexError:
            return {}

    def __get_hourly_model(self, forecast):
        return {
            "weather_condition": forecast[0]['weather'][0]['id'],
            "current_weather": temperature(forecast[0]['main']['temp']),
            "maximum_temperature": temperature(self.__get_max(forecast)),
            "minimum_temperature": temperature(self.__get_min(forecast)),
            "sun_rise": None,
            "sun_down": None,
            "rain_probability": rain_probability(self.__get_rain_probability(forecast))
        }

    @classmethod
    def __get_current_model(cls, forecast):
        return {
            "weather_condition": forecast['weather'][0]['id'],
            "current_weather": forecast['main']['temp'],
            "maximum_temperature": forecast['main']['temp_max'],
            "minimum_temperature": forecast['main']['temp_min'],
            "sun_rise": None,
            "sun_down": None,
            "rain_probability": 0
        }

    def __get_rain_probability(self, today):
        result_list = []
        for i in today:
            result_list.append(self.__get_item_rain_probability(i))
        return max(result_list)

    @classmethod
    def __get_item_rain_probability(cls, today):
        try:
            if today['rain'] and today['rain']['3h']:
                return today['rain']['3h'] * 100
            else:
                return 0
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
        max_list = []
        for i in forecast_list:
            max_list.append(i['main']['temp_max'])
        return max(max_list)
