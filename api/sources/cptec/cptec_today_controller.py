from flask_restful import Resource

from api.sources.cptec.cptec_model import CptecModel


class CPTECTodayController(Resource):

    def __init__(self):
        self.__model = CptecModel()

    def get(self, region, city):
        return self.__model.make_site_request(region, city).get_today_resume()
