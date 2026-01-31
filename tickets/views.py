from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse
from django.shortcuts import get_object_or_404

from attendees.models import Attendee
from events.models import Event
from tickets.models import Ticket
from tickets.serializers import TicketSerializer
from tickets.services.ticket_service import create_ticket


class TicketCreateView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        attendee_id = request.data.get("attendee_id")
        event_id = request.data.get("event_id")

        if not attendee_id or not event_id:
            return Response(
                {"error": "attendee_id and event_id are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        attendee = get_object_or_404(Attendee, id=attendee_id)
        event = get_object_or_404(Event, id=event_id)

        try:
            ticket = create_ticket(event=event, attendee=attendee)
        except Exception as e:
            return Response(
                {"error": "Ticket creation failed"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            TicketSerializer(ticket).data,
            status=status.HTTP_201_CREATED
        )


class TicketPDFDownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, ticket_code):
        ticket = get_object_or_404(Ticket, numeric_code=ticket_code)

        if not ticket.pdf_ticket:
            return Response(
                {"error": "PDF not available"},
                status=status.HTTP_404_NOT_FOUND
            )

        return FileResponse(
            open(ticket.pdf_ticket.path, "rb"),
            content_type="application/pdf"
        )
