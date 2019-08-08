import mongoengine


class SourceUri(mongoengine.EmbeddedDocument):
    api = mongoengine.StringField()
    site = mongoengine.StringField()
