from rest_framework import serializers


class CancelSerializer(serializers.Serializer):
    exit_game = serializers.BooleanField()
    user = serializers.CharField()
