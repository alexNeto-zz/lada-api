import datetime

import mongoengine

from api.services.ranking import default_rank


class Vote(mongoengine.Document):
    location = mongoengine.StringField()
    source_name = mongoengine.StringField()
    up_vote = mongoengine.IntField()
    down_vote = mongoengine.IntField()
    score = mongoengine.FloatField(default=default_rank)
    update_at = mongoengine.DateTimeField(default=datetime.datetime.now)
    created_at = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'votes'
    }
