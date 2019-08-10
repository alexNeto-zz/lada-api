import mongoengine

from api.storage.uri import Uri


class SourceUri(mongoengine.EmbeddedDocument):
    api = mongoengine.EmbeddedDocumentField(Uri)
    site = mongoengine.EmbeddedDocumentField(Uri)
