from api.storage.source import Source


class SourceDataService:
    @classmethod
    def create_source(cls, source: Source):
        source.save()
        return source

    @classmethod
    def find_all(cls):
        return Source.objects()

    @classmethod
    def find_by_source_name(cls, source_name: str):
        return Source.objects().filter(source_name=source_name).first()

    @classmethod
    def find_by_country(cls, country: str):
        result = Source.objects(country_available__in=['*', country.upper()])
        return result if result is not None else Source()
