import os

from flask_restful import Resource


class TestController(Resource):

    def get(self):
        return {
            'test': os.environ.get('TEST', 'NONE')
        }
