from api.storage.source import Source


class SourceDataService:
    @staticmethod
    def create_source(source: Source):
        source.save()
        return source

    @staticmethod
    def find_all():
        return Source.objects()

    @staticmethod
    def find_by_source_name(source_name: str):
        return Source.objects().filter(source_name=source_name).first()
