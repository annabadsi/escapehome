import json

from core.models import Riddle
from escapehome import settings


def create_json(riddle: Riddle):
    with open(f'{settings.PROJECT_DIR}/escapehome/api/resources/protocol_commands.json', 'w') as json_file:
        json.dump(riddle.as_json(), json_file, indent=2)
