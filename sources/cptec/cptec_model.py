from sources.cptec.getter.cptec_api_getter import CptecAPIGetter
from sources.cptec.getter.cptec_getter import CptecGetter
from sources.cptec.normalizer.cptec_normalizer import CptecNormalizer


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
        return CptecNormalizer(self.__today_data).get_resume()

    def get_today_complete(self):
        pass

    def get_week_resume(self):
        return CptecNormalizer(self.__week_data).get_week_resume()

    def get_week_complete(self):
        pass
