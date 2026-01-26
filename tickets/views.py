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
from .qr import generate_ticket_qr
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from tickets.services.ticket_service import create_ticket

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

        ticket = create_ticket(event=event, attendee=attendee)

        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class TicketPDFDownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, ticket_code):
        ticket = get_object_or_404(Ticket, numeric_code=ticket_code)

        if not ticket.pdf_ticket:
            return Response({"error": "PDF not available"}, status=404)

        return FileResponse(
            open(ticket.pdf_ticket.path, "rb"),
            content_type="application/pdf"
        )

# Create your views here.
