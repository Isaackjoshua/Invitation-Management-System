from rest_framework import serializers

class CheckInSerializer(serializers.Serializer):
    ticket_code = serializers.CharField(max_length=8)