import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ReadySerializer
from core.models import Riddle
from escapehome import settings


@api_view(['POST'])
def ready(request):
    serializer = ReadySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    print(serializer.validated_data['text'])

    return Response(status=200, data=["nichts!"])


@api_view(['POST', 'GET'])
def commands(request):
    try:
        with open(f'{settings.PROJECT_DIR}/escapehome/api/resources/protocol_commands.json') as json_file:
            data = json.load(json_file)
    except:
        print("Fehler!")
        data = {}

    return Response(status=200, data=data)


def create_json(riddle: Riddle):
    with open(f'{settings.PROJECT_DIR}/escapehome/api/resources/protocol_commands.json', 'w') as json_file:
        if riddle.commands.all():
            json.dump(
                riddle.as_json(),
                json_file,
                indent=2
            )
        else:
            json.dump(
                {},
                json_file
            )
