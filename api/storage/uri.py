import mongoengine


class Uri(mongoengine.EmbeddedDocument):
    address = mongoengine.StringField()
    params = mongoengine.StringField()
