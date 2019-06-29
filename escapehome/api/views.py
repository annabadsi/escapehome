from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ReadySerializer


@api_view(['POST'])
def ready(request):
    serializer = ReadySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    print(serializer.validated_data['text'])

    return Response(status=200, data=["nichts!"])
