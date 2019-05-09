from sources.cptec.auxiliar_information_enum import Auxiliar, Temperature


class CPTECScrapy:

    def __init__(self, parsed_html):
        self.__data = parsed_html

    def get_maximum_temperature(self):
        return self.__get_today_temperature(minimum=True)

    def get_minimum_temperature(self):
        return self.__get_today_temperature(minimum=False)

    def get_sun_rise(self):
        return self.__get_auxiliar_informatin(Auxiliar.SUN_RISE)

    def get_sun_down(self):
        return self.__get_auxiliar_informatin(Auxiliar.SUN_DOWN)

    def get_rain_probability(self):
        return self.__get_auxiliar_informatin(Auxiliar.RAIN_PROBABILITY)

    def get_maximum_UV(self):
        return self.__get_auxiliar_informatin(Auxiliar.MAXIMUM_UV)

    def __get_auxiliar_informatin(self, index):
        return self.__trim(self.__data.find_all(attrs="col-md-4 text-center align-middle")[index.value].span.text)

    @staticmethod
    def __trim(text):
        return text.strip("\xa0").replace("°", "")

    def __get_today_temperature_container(self):
        return self.__data.find_all(attrs='temperaturas')[0]

    def __get_today_temperature(self, minimum=True):
        return self.__trim(self.__get_today_temperature()
                           .find_all(name='span')[Temperature.MINIMUM if minimum else Temperature.MAXIMUM]
                           .text)