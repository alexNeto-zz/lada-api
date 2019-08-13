import os

import mongoengine
import sentry_sdk


def global_init():
    mongoengine.connect(alias='core',
                        db='heroku_x6jxgkt0',
                        host=os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/heroku_x6jxgkt0'))

    sentry_sdk.init(dsn=os.environ.get('SENTRY_DSN', ''), release="lada-api@0.0.0")
