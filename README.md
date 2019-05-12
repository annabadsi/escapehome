# EscapeHome
escape game for your own home with Smart Home devices

# Installation 
You can Setup the Project in two Ways: 
* with Docker
* with a virtual env
### Docker
Navigate to the root folder and just type: 

```shell
make run
```

This can take a longer time so grab you a coffee ☕

### local setup
If you do not want to use Docker you have to setup by your own

1. create a virtual env and active 
```shell
virtualenv venv --python=python3
. venv/bin/activate
# Your terminal should have (venv) in front
```
2. install requirements
```shell
pip install -r requirements.txt
```

# Quick start
If you want to use docker type `export USE=docker` in your terminal

Django always need a Server running so type: 
```shell
make run
```

If the makefile is broke you can type in: 
```shell
docker-compose up -d 
```
or for your local installation

```shell
cd escapehome
python manage.py runserver
```

# Helpful 
* [Django Tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
