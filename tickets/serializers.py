from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    attendee_name = serializers.CharField(
        source="attendee.full_name", read_only=True
    )
    event_name = serializers.CharField(
        source="event.name", read_only=True
    )

    class Meta:
        model = Ticket
        fields = (
            "id",
            "event",
            "event_name",
            "attendee",
            "attendee_name",
            "numeric_code",
            "is_checked_in",
            "checked_in_at",
            "created_at",
        )
        read_only_fields = (
            "id",
            "numeric_code",
            "is_checked_in",
            "checked_in_at",
            "created_at",
        )