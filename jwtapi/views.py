from django.shortcuts import render
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
        '/get/users/all/',
        '/get/user/<string:serial>/',
        '/get/meeting/all/',
        '/get/attendances/all/',
        '/mark/attendance/',
    ]
    return Response(routes)
@api_view(['POST'])
def mark_attendance(request):
    data = request.data
    meeting = Meeting.objects.get(id=data['meeting_id'])
    user = NFCUser.objects.get(id=data['user_id'])
    attendance = Attendance.objects.filter(meeting=meeting, user=user).first()

    if attendance:
        attendance.status = data['status']
        formatted_date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
        attendance.date = formatted_date
        attendance.save()
    else:
        formatted_date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
        attendance = Attendance.objects.create(
            meeting=meeting,
            user=user,
            status=data['status'],
            date=formatted_date
        )

    # Return a status code as response
    return Response(status=status.HTTP_200_OK)
        
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
        return Attendance.objects.all()