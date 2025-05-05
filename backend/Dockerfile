FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY backend/requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install python-decouple

COPY ./compose/local/start.sh /
RUN chmod +x /start.sh
RUN export DJANGO_SETTINGS_MODULE=backend.settings.local
COPY backend/ /app/