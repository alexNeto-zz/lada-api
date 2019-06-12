import json

from api.sources.cptec.cptec_model import CptecModel


class TodayResumeModel:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_today_resume_list(self):
        return json.dumps([
            CptecModel(self.__x, self.__y).make_request().get_today_resume(),
        ])
