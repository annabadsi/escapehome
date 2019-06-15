FROM python:3

ENV PYTHONUNBUFFERED 1
ENV ALEXA_APP_ID_escapehome="amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29"
ENV ALEXA_REQUEST_VERIFICATON="False"
ENV DEBUG="True"
RUN mkdir /escapehome
WORKDIR /escapehome
COPY requirements_docker.txt /escapehome/
RUN pip install -r requirements_docker.txt
RUN export DJANGO_SETTINGS_MODULE=escapehome.settings.docker
COPY . /escapehome/