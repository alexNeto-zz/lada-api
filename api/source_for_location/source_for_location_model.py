from api.source.source_data_service import SourceDataService


class SourceForLocationModel:

    def __init__(self):
        self.__data_service = SourceDataService()

    def get_for_location(self, country: str):
        result = self.__data_service.find_by_country(country)
        return self.__make_source_name_list(result) if result is not None else []

    @staticmethod
    def __make_source_name_list(sources):
        source_list = []
        for source in sources:
            source_list.append(source.source_name)
        return source_list
