from api.source.source_data_service import SourceDataService
from api.storage.source import Source


class SourceForLocationModel:

    def __init__(self):
        self.__data_service = SourceDataService()

    def get_for_location(self, country: str):
        result = Source.objects(country_available=country.upper())
        return result if result is not None else Source()
