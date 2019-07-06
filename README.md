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
# enviroment varibales
to set the Alexa-Skill id go to the projectfolder (escapehome) and add the var ALEXA_APP_ID_escapehome to the new Alexa-Skill ID at the .env file (if you can not see it remember its a hidden file :D )

# Endpoints
1. POST - `api/ready`  
Body: `{"text":"was gibt es neues?"}`

# Alexa Skill Management

## ASK CLI
Alexa Skills Kit Command Line Interface  
https://developer.amazon.com/docs/smapi/quick-start-alexa-skills-kit-command-line-interface.html


**get-skill** 
```
ask api get-skill -s amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29 --stage development > json/skill.json
```

**get-model**
```
ask api get-model -s amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29 --stage development -l de-DE > json/model.json
```

**update-model**
```
ask api update-model -s amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29 -f json/model.json -l de-DE --stage development
```

**get-skill-status**
```
ask api get-skill-status -s amzn1.ask.skill.e5c0051e-6fcc-4c73-9a22-9487ee9b0d29
```

### Update Custom Slot Types
1. `make get-model`
2. copy code `scripts/model_dump.py` in python console
3. `make update-model`
4. `make skill-status`

## SMAPI
Skill Management API
https://developer.amazon.com/docs/smapi/smapi-overview.html

**[get-skill](https://developer.amazon.com/docs/smapi/skill-operations.html#get-skill-information)**
```
GET  /v1/skills/{skillId}/stages/{stage}/manifest
```

**[get-model](https://developer.amazon.com/docs/smapi/interaction-model-operations.html#get-interaction-model)**
```
GET /v1/skills/{skillId}/stages/{stage}/interactionModel/locales/{locale}
```

**[update-model](https://developer.amazon.com/docs/smapi/interaction-model-operations.html#update-interaction-model)**
```
PUT /v1/skills/{skillId}/stages/{stage}/interactionModel/locales/{locale}
```

**[get-skill-status](https://developer.amazon.com/docs/smapi/skill-operations.html#get-skill-status)**
```
GET /v1/skills/{skillId}/status?resource={resource1}&resource={resource2}
```

# Locales Arbeiten mit Alexa
__NGROK einrichten__
* ngrok runterladen > https://ngrok.com/download
* starten: `./ngrok http 8000`
* generierte URL kopieren
    * in Alexa Developer Console > Entpoints anpassen `https://<nummer>.ngrok.io/alexa/`, zweites Auswahlfeld beachten
    * `<nummer>.ngrok.io` (ohne https) zu `ALLOWED_HOSTS` in settings `common.py` hinzufügen
* Django starten (mit oder ohne Docker)

__Daten aus dem Dump übertagen__
* `python manage.py migrate`
* `python manage.py shell` 
* Enter the following in the shell
  ```shell
  from django.contrib.contenttypes.models import ContentType
  ContentType.objects.all().delete()
  ```
* `python manage.py loaddata db_dump.json`
