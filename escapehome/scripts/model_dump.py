# TODO: Dump automatisch nach DB Ändernungen in JSON-Datei von Skill speichern und updaten
# TODO  SMAPI verwenden (OAuth (Login with Amazon): https://developer.amazon.com/docs/smapi/smapi-overview.html
import json
from django.apps import apps

PATH = 'json/model.json'
MODEL_NAME = 'Scenario'
FIELD_NAME = 'name'

model = apps.get_model('core', MODEL_NAME)
types = model.objects.values_list(FIELD_NAME, flat=True)

skill_model = json.loads(open(PATH).read())
for slot_type in skill_model['interactionModel']['languageModel']['types']:
    if slot_type['name'] == f'ESCAPEHOME_{MODEL_NAME}':
        slot_type['values'] = [
            {'name': {'value': t}}
            for t in types
        ]

with open(PATH, 'w', encoding='utf-8') as json_file:
    json.dump(skill_model, json_file, ensure_ascii=False, indent=2)
