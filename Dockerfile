#FROM ubuntu:20.04
FROM python:3.9-buster

ARG DEBIAN_FRONTEND=noninteractive

#RUN apt-get update &&  \
#    apt-get install --no-install-recommends -y python3.9 python3.9-dev  \
#    python3.9-venv python3-pip python3-wheel build-essential && \
#	apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#ARG APP_USER=vincent
#RUN adduser -D ${APP_USER}

WORKDIR /usr/src/app
COPY . .
EXPOSE 8000

RUN pip --no-cache install -r requirements.txt && python3 manage.py collectstatic --noinput

#CMD python manage.py runserver

#RUN ['gunicorn', '--env', 'DJANGO_SETTINGS_MODULE=oc_lettings_site.settings', 'oc_lettings_site.wsgi', '-w', '4', '-b', ':8000', '--reload', '--timeout', '300']
