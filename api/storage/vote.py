import datetime

import mongoengine


class Vote(mongoengine.Document):
    location = mongoengine.StringField()
    up_vote = mongoengine.FloatField()
    down_vote = mongoengine.FloatField()
    update_at = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'votes'
    }
