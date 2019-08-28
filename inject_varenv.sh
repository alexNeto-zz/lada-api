#!/usr/bin/env bash

echo "injecting varenv"

{
  printf "\nenv_variables:\n"
  printf "\tMONGODB_URI: '%s'\n" "$MONGODB_URI"
  printf "\tOPEN_WEATHER_TOKEN: '%s'\n" "$OPEN_WEATHER_TOKEN"
  printf "\tSENTRY_DSN: '%s'\n" "$SENTRY_DSN"
  printf "\tTESTE: '%s'\n" "AAAAAAAAAAA"
} >>app.yaml

echo "done"