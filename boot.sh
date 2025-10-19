#!/bin/sh
set -e
sleep 5
exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app
