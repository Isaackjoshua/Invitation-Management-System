from rest_framework import serializers
from .models import Attendee

class AttendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = "__all__"
        read_only_fields = ("id", "created_at")
