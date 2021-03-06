import mongoengine


class Conditions(mongoengine.EmbeddedDocument):
    cloudy = mongoengine.ListField()
    cloudy_day_1 = mongoengine.ListField()
    cloudy_day_2 = mongoengine.ListField()
    cloudy_day_3 = mongoengine.ListField()
    cloudy_night_1 = mongoengine.ListField()
    cloudy_night_2 = mongoengine.ListField()
    cloudy_night_3 = mongoengine.ListField()
    day = mongoengine.ListField()
    night = mongoengine.ListField()
    rainy_1 = mongoengine.ListField()
    rainy_2 = mongoengine.ListField()
    rainy_3 = mongoengine.ListField()
    rainy_4 = mongoengine.ListField()
    rainy_5 = mongoengine.ListField()
    rainy_6 = mongoengine.ListField()
    rainy_7 = mongoengine.ListField()
    snowy_1 = mongoengine.ListField()
    snowy_2 = mongoengine.ListField()
    snowy_3 = mongoengine.ListField()
    snowy_4 = mongoengine.ListField()
    snowy_5 = mongoengine.ListField()
    snowy_6 = mongoengine.ListField()
    thunder = mongoengine.ListField()
