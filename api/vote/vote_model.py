from api.services.string_services import dash
from api.source.source_data_service import SourceDataService
from api.storage.vote import Vote


class VoteModel:

    def __init__(self):
        self.__source_data_service = SourceDataService()

    def get_vote_for_source(self, source: str, location: str):
        return self.__get_vote_or_new(source, location).to_json()

    def update_vote_for_source(self, source, location, request_body):
        vote = self.__get_vote_or_new(source.upper(), location)
        if request_body['up_vote']:
            vote.up_vote = vote.up_vote + 1
        if request_body['down_vote']:
            vote.down_vote = vote.down_vote + 1
        vote.save()
        return vote.to_json()

    def __get_vote_or_new(self, source: str, location: str) -> Vote:
        parsed_location = dash(location)
        vote = Vote.objects().filter(source_name=source.upper(), location=parsed_location).first()
        return vote if vote is not None else self.__create_new_vote(source, parsed_location)

    @classmethod
    def __create_new_vote(cls, source: str, location: str) -> Vote:
        vote = Vote()
        vote.source_name = source
        vote.location = location
        vote.up_vote = 0
        vote.down_vote = 0
        vote.save()
        return vote