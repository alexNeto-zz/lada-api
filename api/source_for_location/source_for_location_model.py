from api.source.source_data_service import SourceDataService
from api.storage.source import Source


class SourceForLocationModel:

    def __init__(self):
        self.__data_service = SourceDataService()

    def get_for_location(self, country: str):
        result = self.__data_service.find_by_country(country)
        return self.__make_source_name_list(result) if result is not None else []

    def __make_source_name_list(self, sources):
        source_list = []
        for source in sources:
            source_list.append({
                'source': source.source_name,
                'params': self.__get_api_param(source)
            })
        return source_list

    @classmethod
    def __get_api_param(cls, source: Source):
        if source.source_uri.site.params == '':
            return source.source_uri.api.params
        else:
            return source.source_uri.site.params
