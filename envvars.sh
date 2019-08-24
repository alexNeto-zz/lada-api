#!/usr/bin/env bash
echo "start"
{
  printf "env_variables:\n"
  printf "  MONGODB_URI: %s\n" "$MONGODB_URI"
  printf "  OPEN_WEATHER_TOKEN: %s\n" "$OPEN_WEATHER_TOKEN"
  printf "  SENTRY_DSN: %s\n" "$SENTRY_DSN"
} >>app.yaml
echo "end"
