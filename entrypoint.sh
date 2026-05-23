#!/bin/sh
set -e

mkdir -p /app/data/media

python manage.py migrate --noinput

exec gunicorn appKeres.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers ${GUNICORN_WORKERS:-2} \
    --timeout ${GUNICORN_TIMEOUT:-120} \
    --access-logfile - \
    --error-logfile -
