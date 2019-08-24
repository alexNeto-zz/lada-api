#!/usr/bin/env bash
echo "start"

echo "injecting variables"
{
  printf "\nenv_variables:\n"
  printf "  MONGODB_URI: '%s'\n" "$MONGODB_URI"
  printf "  OPEN_WEATHER_TOKEN: '%s'\n" "$OPEN_WEATHER_TOKEN"
  printf "  SENTRY_DSN: '%s'\n" "$SENTRY_DSN"
  printf "  TEST: '%s'\n" "AAAAAAAAAAA"
} >>app.yaml
echo "end"
