import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CancelSerializer
from core.models import Riddle, ActiveScenario, Command
from escapehome import settings


@api_view(['POST', 'GET'])
def commands(request):
    try:
        with open(f'{settings.PROJECT_DIR}/escapehome/api/resources/protocol_commands.json') as json_file:
            data = json.load(json_file)
    except:
        print("Fehler!")
        data = {}

    return Response(status=200, data=data)


# Modbus: Magnet hat kontakt verloren (Box offen), Spiel abbrechen!
@api_view(['POST'])
def cancel(request):
    serializer = CancelSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    exit_game = serializer.validated_data['exit_game']
    user = serializer.validated_data['user']

    if exit_game:
        active_scenario = ActiveScenario.objects.get(user=user)
        active_scenario.box = True
        active_scenario.save()

    return Response(status=200, data=None)


def create_json(data: dict):
    with open(f'{settings.PROJECT_DIR}/escapehome/api/resources/protocol_commands.json', 'w') as json_file:
        json.dump(
            data,
            json_file,
            indent=2
        )


def riddle_commands_to_json(riddle: Riddle, user_id: str):
    if riddle.commands.all():
        create_json(riddle.as_json(user_id))
    else:
        create_json({})


def box_command_to_json(command: Command, user_id: str, ):
    create_json(
        {
            'meta':
                {
                    'loop': 1,
                    'user_id': user_id
                },
            'commands': [
                command.as_json()
            ]
        }
    )
