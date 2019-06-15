from rest_framework import serializers


class ReadySerializer(serializers.Serializer):
    text = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
