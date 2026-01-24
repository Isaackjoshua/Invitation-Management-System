from django.shortcuts import render
from rest_framework import generics
from accounts.permissions import IsAdmin
from .models import Attendee
from .serializers import AttendSerializer

class AttendeeListCreateView(generics.ListCreateAPIView):
    queryset = Attendee.objects.all()
    serializer_class = AttendSerializer
    permission_classes = [IsAdmin]
    
# Create your views here.
