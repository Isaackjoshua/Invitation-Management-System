from django.urls import path
from .views import TicketCheckInView
from .admin_views import EventStatsView

urlpatterns = [
    path("scan/", TicketCheckInView.as_view()),
    path("stats/", EventStatsView.as_view()),

]