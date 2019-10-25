from flask_restful import Resource

from api.about.about_service import AboutService


class AboutController(Resource):

    def __init__(self):
        self.__model = AboutService()

    def get(self):
        return self.__model.get_version()

    def put(self, project, version):
        return self.__model.put_version(project, version)
