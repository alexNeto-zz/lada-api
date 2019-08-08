from api.source.source_data_service import SourceDataService
from api.storage.source import Source


class SourceModel:

    def __init__(self):
        self.__data_service = SourceDataService()

    def get_by_source_name(self, source_name: str) -> Source:
        result = self.__data_service.find_by_source_name(source_name.upper())
        return result if result is not None else Source()

    def get_source_list(self):
        return self.__data_service.find_all()

    def new_source(self, source_name: str, new_source: Source):
        return new_source.save()
