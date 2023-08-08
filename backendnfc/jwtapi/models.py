from django.db import models
from .choices import *
class NFCUser(models.Model):
    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField()
    nfc_serial = models.CharField(max_length=100, unique=True)
    roll_no = models.CharField(max_length=100)
    faculty_registered = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class Meeting(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    club = models.CharField(max_length=100,default="MIC")
    
    def __str__(self):
        return f"{self.name} - {self.club}"

class Attendance(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    nfcuser = models.ForeignKey(NFCUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="Absent")
    date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.nfcuser.username} - {self.meeting.name} - {self.meeting.club}"
