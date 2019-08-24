#!/usr/bin/env bash

echo -e "injecting vars"

echo -e "env_variables:" >>app.yaml
echo -e "\n" >>app.yaml
echo -e "\tMONGODB_URI: $MONGODB_URI\n" >>app.yaml
echo -e "\tOPEN_WEATHER_TOKEN: $OPEN_WEATHER_TOKEN\n" >>app.yaml
echo -e "\tSENTRY_DSN: $SENTRY_DSN" >>app.yaml

cat app.yaml
echo -e "done injecting"