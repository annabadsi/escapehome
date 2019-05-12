FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /escapehome
WORKDIR /escapehome
COPY requirements_docker.txt /escapehome/
RUN pip install -r requirements_docker.txt
RUN export DJANGO_SETTINGS_MODULE=escapehome.settings.docker
COPY . /escapehome/