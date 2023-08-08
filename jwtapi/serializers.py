from .models import *
from rest_framework import serializers


class NFCUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFCUser
        fields = ("__all__")

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ("__all__")

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ("__all__")