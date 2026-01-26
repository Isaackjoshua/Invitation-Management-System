from django.urls import path
from .views import TicketCreateView, TicketPDFDownloadView

urlpatterns = [
    
    path("<str:ticket_code>/pdf/", TicketPDFDownloadView.as_view()),
    path("generate/", TicketCreateView.as_view()),
]