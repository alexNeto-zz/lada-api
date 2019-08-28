import os

from flask_restful import Resource

from api.api_setup import get_api_version, get_app_version


class AboutController(Resource):

    def get(self):
        return {
            "app_version": get_app_version(),
            "api_version": get_api_version()
        }
