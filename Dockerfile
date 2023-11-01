FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY . .
EXPOSE 8000

RUN pip --no-cache install -r requirements.txt && python3 manage.py collectstatic --noinput
CMD gunicorn --env DJANGO_SETTINGS_MODULE=oc_lettings_site.settings oc_lettings_site.wsgi -w 4 -b 0.0.0.0:$PORT --reload --timeout 300
