from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permissions import IsAdmin
from tickets.models import Ticket
from checkins.models import CheckIn

class EventStatsView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({
            "total_tickets": Ticket.objects.count(),
            "checked_in": Ticket.objects.filter(is_checked_in=True).count(),
            "not_checked_in": Ticket.objects.filter(is_checked_in=False).count(),
            "total_checkins": CheckIn.objects.count(),
        })
