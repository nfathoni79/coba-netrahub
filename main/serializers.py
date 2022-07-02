from rest_framework import serializers


class UpSerializer(serializers.Serializer):
    payload = serializers.CharField()
    dataType = serializers.CharField()
