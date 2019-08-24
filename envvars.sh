#!/usr/bin/env bash
echo "start"

echo "injecting variables"
{
  printf "\nenv_variables:\n"
  printf "\tMONGODB_URI: '%s'\n" "$MONGODB_URI"
  printf "\tOPEN_WEATHER_TOKEN: '%s'\n" "$OPEN_WEATHER_TOKEN"
  printf "\tSENTRY_DSN: '%s'\n" "$SENTRY_DSN"
} >>app.yaml
echo "end"
