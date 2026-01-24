from django.urls import path
from .views import TicketCreateView

urlpatterns = [
    path("generate/", TicketCreateView.as_view()),
]