import os

import sentry_sdk
from mongoengine import connect


def global_init():
    print(os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/lada-db'))
    connect(
        alias='core',
        db='lada-db',
        host=os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/lada-db')
    )

    sentry_sdk.init(dsn=os.environ.get('SENTRY_DSN', ''), release="lada-api@" + get_api_version())


def get_app_version():
    return "0.0.4"


def get_api_version():
    return "0.0.3"
