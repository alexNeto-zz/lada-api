#!/usr/bin/env bash

echo -e "injecting vars"
echo -e "runtime: python37" >>app.yaml
echo -e "env_variables:" >>app.yaml
echo -e "  MONGODB_URI: $MONGODB_URI" >>app.yaml
echo -e "  OPEN_WEATHER_TOKEN: $OPEN_WEATHER_TOKEN" >>app.yaml
echo -e "  SENTRY_DSN: $SENTRY_DSN" >>app.yaml

cat app.yaml
echo -e "done injecting"