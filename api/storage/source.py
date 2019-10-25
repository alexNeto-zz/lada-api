import datetime

import mongoengine

from api.storage.conditions import Conditions
from api.storage.source_uri import SourceUri


class Source(mongoengine.Document):
    source_name = mongoengine.StringField()
    source_uri = mongoengine.EmbeddedDocumentField(SourceUri)
    country_available = mongoengine.ListField()
    conditions = mongoengine.EmbeddedDocumentField(Conditions)
    update_at = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'sources'
    }
