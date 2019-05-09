from sources.cptec.scrapy.cptec_scrapy import CPTECScrapy


class CPTECNormalizer:

    def __init__(self, data):
        self.__scrapy = CPTECScrapy(data)

    def get_resume(self):
        return {
            "maximum_temperature": self.__scrapy.get_maximum_temperature(),
            "minimum_temperature": self.__scrapy.get_minimum_temperature(),
            "sun_rise": self.__scrapy.get_sun_rise(),
            "sun_down": self.__scrapy.get_sun_down(),
            "rain_probability": self.__scrapy.get_rain_probability()
        }
