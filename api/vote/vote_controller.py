import json

from flask_restful import Resource, reqparse

from api.vote.vote_model import VoteModel


class VoteController(Resource):
    def __init__(self):
        self.__model = VoteModel()
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('up_vote', type=bool)
        self.__parser.add_argument('down_vote', type=bool)

    def get(self, source, location):
        return json.loads(self.__model.get_vote_for_source(source, location))

    def put(self, source, location):
        return json.loads(self.__model.update_vote_for_source(source, location, self.__parser.parse_args()))
