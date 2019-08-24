#!/usr/bin/env bash
echo "start"

echo "injecting variables"
cat <<EOF >>app.yaml
env_variables:
  MONGODB_URI: $MONGODB_URI
  OPEN_WEATHER_TOKEN: $OPEN_WEATHER_TOKEN
  SENTRY_DSN: $SENTRY_DSN
  TEST: AAAAAAAAAAA
EOF
#echo "teste %s" "$AAA"
#{
#  printf "\nenv_variables:\n"
#  printf "  MONGODB_URI: '%s'\n" "$MONGODB_URI"
#  printf "  OPEN_WEATHER_TOKEN: '%s'\n" "$OPEN_WEATHER_TOKEN"
#  printf "  SENTRY_DSN: '%s'\n" "$SENTRY_DSN"
#  printf "  TEST: '%s'\n" "AAAAAAAAAAA"
#} >>app.yaml
echo "end"
