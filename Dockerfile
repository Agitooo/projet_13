FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY . .
EXPOSE 8000

RUN pip --no-cache install -r requirements.txt && python3 manage.py collectstatic --noinput
