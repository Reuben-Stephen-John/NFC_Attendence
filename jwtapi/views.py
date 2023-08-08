from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view
from rest_framework import generics
# Create your views here.





## Function Based Views
@api_view(['GET'])
def get_routes(request):
    routes = [
        '/get/users/all/',
        '/get/user/<string:serial>/',
        '/get/meeting/all/',
        '/get/attendances/all/',
        '/mark/attendance/',
    ]
    return Response(routes)

## Class Based Views
class NFCUserAPIView(generics.ListCreateAPIView):
    model = NFCUser
    permission_classes = [IsAdminUser]
    serializer_class = NFCUserSerializer
    
    def get_queryset(self):
        return NFCUser.objects.all()
    
class MeetingAPIView(generics.ListCreateAPIView):
    model = Meeting
    permission_classes = [IsAdminUser]
    serializer_class = MeetingSerializer
    
    def get_queryset(self):
        return Meeting.objects.all()
    
class AttendanceAPIView(generics.ListCreateAPIView):
    model = Attendance
    permission_classes = [IsAdminUser]
    serializer_class = AttendanceSerializer
    def get_queryset(self):
        return Attendance.objects.all()