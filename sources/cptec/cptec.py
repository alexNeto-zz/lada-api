from flask import Blueprint

from sources.cptec.getter.cptec_getter import CPTECGetter
from sources.cptec.normalizer.cptec_normalizer import CPTECNormalizer

test_blueprint = Blueprint('test', __name__)


@test_blueprint.route("/today_resume/<string:country>/<string:state>/<string:city>")
def today_resume(country, state, city):
    return CPTECModel(country, state, city).make_request().get_today_resume()


@test_blueprint.route("/today_complete/<string:country>/<string:state>/<string:city>")
def today_complete(country, state, city):
    return CPTECModel(country, state, city).make_request().get_today_complete()


@test_blueprint.route("/week_resume/<string:country>/<string:state>/<string:city>")
def week_resume(country, state, city):
    return CPTECModel(country, state, city).make_request().get_week_resume()


@test_blueprint.route("/week_complete/<string:country>/<string:state>/<string:city>")
def week_complete(country, state, city):
    return CPTECModel(country, state, city).make_request().get_week_complete()


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
