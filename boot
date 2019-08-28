#!/usr/bin/env bash

exec gunicorn -b :5000 --access-logfile - --error-logfile - main:app
