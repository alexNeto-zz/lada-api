import datetime

import mongoengine


class Vote(mongoengine.Document):
    location = mongoengine.StringField()
    source_name = mongoengine.StringField()
    up_vote = mongoengine.IntField()
    down_vote = mongoengine.IntField()
    update_at = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'votes'
    }
