from django.contrib import admin
from .models import NFCUser,Attendance,Meeting
# Register your models here.
admin.site.register(NFCUser)
admin.site.register(Attendance)
admin.site.register(Meeting)
