from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import IsAdmin
from .models import Ticket
from .serializers import TicketSerializer
from .utils import generate_numeric_code
from attendees.models import Attendee
from events.models import Event

class TicketCreateView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        attendee_id = request.data.get("attendee_id")
        event_id = request.data.get("event_id")

        if not attendee_id or not event_id:
            return Response(
                {"error": "attendee_id and event_id are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        attendee = Attendee.objects.get(id=attendee_id)
        event = Event.objects.get(id=event_id)

        ticket = Ticket.objects.create(
            attendee=attendee,
            event=event,
            numeric_code = generate_numeric_code(),
        )

        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# Create your views here.
