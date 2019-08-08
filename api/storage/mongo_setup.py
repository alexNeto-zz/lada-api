import os

import mongoengine


def global_init():
    mongoengine.connect(alias='core',
                        db='heroku_x6jxgkt0',
                        host=os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/heroku_x6jxgkt0'))
