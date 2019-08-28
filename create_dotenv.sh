#!/usr/bin/env bash

echo "creating .env"

echo MONGODB_URI=$MONGODB_URI >>.env
echo OPEN_WEATHER_TOKEN=$OPEN_WEATHER_TOKEN >>.env
echo SENTRY_DSN=$SENTRY_DSN >>.env
echo TESTE=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa >> .env

echo "created .env"