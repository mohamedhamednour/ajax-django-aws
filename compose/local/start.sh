#!/bin/bash

python manage.py migrate

python manage.py collectstatic --noinput

# Run development server
python manage.py runserver 0.0.0.0:8000
