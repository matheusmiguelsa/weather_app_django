
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /cb_dj_weather_app

WORKDIR /cb_dj_weather_app

ADD . /cb_dj_weather_app/

RUN pip install -r requirements.txt