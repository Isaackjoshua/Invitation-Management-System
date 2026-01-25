from django.db import transaction
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsStaff
from tickets.models import Ticket
from .models import CheckIn
from .serializers import CheckInSerializer


# Create your views here.
class TicketCheckInView(APIView):
    permission_classes = [IsStaff]

    @transaction.atomic
    def post(self, request):
        serializer = CheckInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ticket_code = serializer.validated_data["ticket_code"]

        try:
            ticket = (
                Ticket.objects
                .select_for_update()
                .select_related("attendee", "event")
                .get(numeric_code=ticket_code)
            )
        except Ticket.DoesNotExist:
            return Response(
                {"status": "INVALID", "message": "Ticket not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        if not ticket.event.is_active:
            return Response (
                {"status": "INVALID", "message": "Event is not active"},
                status=status.HTTP_400_BAD_REQUEST,

            )
        
        if ticket.is_checked_in:
            return Response(
                {
                    "status": "ALREADY_CHECKED_IN",
                    "attendee": ticket.attendee.full_name,
                    "checked_in_at": ticket.checked_in_at,
                },
                status=status.HTTP_409_CONFLICT,
            )
        
        #Perform check-in
        ticket.is_checked_in = True
        ticket.checked_in_at = timezone.now()
        ticket.save()

        CheckIn.objects.create(
            ticket=ticket,
            staff=request.user
        )

        return Response(
            {
                "status": "SUCCESS",
                "attendee": ticket.attendee.full_name,
                "event": ticket.event.name,
                "checked_in_at": ticket.checked_in_at,
            },
            status=status.HTTP_200_OK,
        )
    