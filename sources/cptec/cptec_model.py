from sources.cptec.getter.cptec_getter import CPTECGetter
from sources.cptec.normalizer.cptec_normalizer import CPTECNormalizer


class CPTECModel:

    def __init__(self, country, state, city):
        self.country = country
        self.state = state
        self.city = city
        self.__data = None

    def make_request(self):
        self.__data = CPTECGetter(self.state, self.city).make_request()
        return self

    def get_today_resume(self):
        return CPTECNormalizer(self.__data).get_resume()

    def get_today_complete(self):
        pass

    def get_week_resume(self):
        pass

    def get_week_complete(self):
        pass
