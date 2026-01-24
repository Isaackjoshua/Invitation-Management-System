from django.urls import path
from .views import AttendeeListCreateView

urlpatterns = [
    path("", AttendeeListCreateView.as_view()),
]