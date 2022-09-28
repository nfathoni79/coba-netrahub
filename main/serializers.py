from rest_framework import serializers


class UpSerializer(serializers.Serializer):
    payload = serializers.CharField()
    dataType = serializers.CharField()


class OngoingSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    payload = serializers.CharField()
    dataType = serializers.CharField(source='data_type')
    status = serializers.IntegerField()


class InboxSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    payload = serializers.CharField()
    dataType = serializers.CharField(source='data_type')
    receivedAt = serializers.SerializerMethodField('get_received_at')

    def get_received_at(self, obj):
        return round(obj.updated_at.timestamp())


class FromDevSerializer(serializers.Serializer):
    dataType = serializers.CharField(source='data_type')
    payload = serializers.CharField()
    bytes = serializers.IntegerField(default=44)
    creditUsage = serializers.IntegerField(default=0)
    transmitTime = serializers.DateTimeField(source='updated_at', format='%y-%m-%d %H:%M:%S')


class ToDevSerializer(serializers.Serializer):
    payload = serializers.CharField()
    dataType = serializers.CharField()
