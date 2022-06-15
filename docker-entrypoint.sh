#!/bin/bash

cd /app/src

python3 manage.py migrate
python3 manage.py bower install
python3 manage.py collectstatic

exec "$@"
