# EscapeHome
Escape Room game for your own home with Smart Home devices. 
Create your own scenario with your Smart Home devices to play with your friends at home! 

Alexa is used to communicate with the players. 
An Alexa Skill was created for this purpose. 
This skill receives instructions via our program, which was deployed on a pythonanywhere server. 
A [Raspberry PI](/pi/README.md) is connected to the Smart Home devices and asks the server for new events. 
If one occurs, it forwards the steps to the respective Smart Home devices. 
Previously, ceiling lamps and blinds were connected via KNX, Philips Hue lamps via Zigbee and a box via Modbus. 
This [box](/box/README.md) serves to lock the room key at the beginning of the game and release it again at the end. 

# README Table of Contents

- [Pythonanywhere](#pythonanywhere)    
- [Installation](#installation)  
- [Quick start](#quick-start)  
- [Endpoints](#endpoints)  
- [Alexa Skill Management](#alexa-skill-management)  
- [Working locally with Alexa](#working-locally-with-alexa)  


- [Box](/box/README.md)
- [Raspberry PI](/pi/README.md)

# Pythonanywhere
We deploy at Pythonanywhere in a free account. That make sometimes some struggle. 
Steps ToDo:
1. start new bash console (console > oher: bash) 
2. start the virtualenv, after that you see the `(venv) at the beginning.
    ```` shell 
    source .virtualenvs/venv/bin/activate
    ````
3. set the pythonanywhere settings
    ``` shell 
    export DJANGO_SETTINGS_MODULE=escapehome.settings.pythonanywhere
    ```
4. get current data:
    ```shell
    git pull
    ```
5. migrate database - can take a few minutes
    ```shell
    cd EscapeHome/escapehome/
    python manage.py migrate
    ```
    

# Installation 
You can Setup the Project in two Ways: 
* with Docker
* with a virtual env


## Docker
Navigate to the root folder and just type: 

```shell
make run
```

This can take a longer time so grab you a coffee ☕

## Local setup
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
**enviroment varibales**
to set the Alexa-Skill id go to the projectfolder (escapehome) and add the var ALEXA_APP_ID_escapehome to the new Alexa-Skill ID at the .env file (if you can not see it remember its a hidden file :D )

# Endpoints
1. GET - `api/commands`  

1. POST - `api/cancel`  
Body: `{"exit_game": "true", "user": "<user_id>"}
`

# Alexa Skill Management 

## ASK CLI
Alexa Skills Kit Command Line Interface  
https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html

**[get-skill](https://developer.amazon.com/docs/smapi/ask-cli-command-reference.html#get-skill-subcommand)** 
```
ask api get-skill -s amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29 --stage development > escapehome/escapehome/static/skill.json
```

**[update-skill](https://developer.amazon.com/docs/smapi/ask-cli-command-reference.html#get-skill-subcommand)** 
```
ask api update-skill -s amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29 --file escapehome/escapehome/static/skill.json --stage development
```

**[get-model](https://developer.amazon.com/docs/smapi/ask-cli-command-reference.html#get-model-subcommand)**
```
ask api get-model -s amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29 --stage development -l de-DE > escapehome/escapehome/static/model.json
```

**[update-model](https://developer.amazon.com/docs/smapi/ask-cli-command-reference.html#update-model-subcommand)**
```
ask api update-model -s amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29 -f escapehome/escapehome/static/model.json -l de-DE --stage development
```

**[get-skill-status](https://developer.amazon.com/docs/smapi/ask-cli-command-reference.html#get-skill-status-subcommand)**
```
ask api get-skill-status -s amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29
```


### Update Custom Slot Types
Copy Relevant Data from DB to Alexa Slot Types  
The first time for authentication: `ask init --no-browser`

Get data from alexa: (only once at the beginning)
1. `make get-model`
2. `make get-skill`

Transfer data from Django to Alexa:
1. `make update-model`
2. `make skill-status`



# Working locally with Alexa
__set up NGROK__
* download ngrok > https://ngrok.com/download
* start `./ngrok http 8000`
* copy generated URL
    * in Alexa Developer Console > customize endpoints `https://<nummer>.ngrok.io/alexa/`, note second checkbox
    * add `<nummer>.ngrok.io` (without https) to `ALLOWED_HOSTS` in settings `common.py`
* start Django (with or without Docker)

__transfer data from the dump__
* `python manage.py migrate`
* `python manage.py shell` 
* Enter the following in the shell
  ```shell
  from django.contrib.contenttypes.models import ContentType
  ContentType.objects.all().delete()
  ```
* `python manage.py loaddata db_dump.json`
