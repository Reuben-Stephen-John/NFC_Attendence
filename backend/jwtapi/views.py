from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from datetime import datetime
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer


## Function Based Views
@api_view(['GET'])
def get_routes(request):
    routes = [
        '/users/',
        '/meeting/',
        '/attendances/',
    ]
    return Response(routes)

        
## Class Based Views
class NFCUserAPIView(generics.ListCreateAPIView):
    model = NFCUser
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
        # Get the meeting_id parameter from the request
        meeting_id = self.request.query_params.get('meeting_id')
        
        # Check if the meeting_id parameter is provided
        if meeting_id is None:
            raise Http404("meeting_id parameter is required.")
        
        # Filter Attendance objects by meeting_id and status='present'
        queryset = Attendance.objects.filter(meeting_id=meeting_id, status='present')
        
        return queryset