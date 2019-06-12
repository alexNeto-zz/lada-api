import json

from api.sources.cptec.cptec_model import CptecModel


class TodayResumeModel:

    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude
        self.__sources = []

    def get_today_resume_list(self):
        self.__append_sources()
        return json.dumps(self.__sources)

    def __append_sources(self):
        self.__append_cptec()

    def __append_cptec(self):
        try:
            self.__sources.append(CptecModel(self.__latitude, self.__longitude).make_request().get_today_resume())
        except IndexError:
            pass
