import os

import sentry_sdk
from mongoengine import connect
from sentry_sdk.integrations.flask import FlaskIntegration

from api.about.about_service import AboutService


def global_init():
    connect(
        alias='core',
        db='lada-db',
        host=os.environ.get('MONGODB_URI', 'mongodb://localhost:27017')
    )

    sentry_sdk.init(
        dsn=os.environ.get('SENTRY_DSN', ''),
        release="lada-api@" + AboutService().api_version(),
        integrations=[FlaskIntegration()]
    )
