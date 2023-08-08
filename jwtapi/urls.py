from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_routes,name="get_routes"),
    path("users/",views.NFCUserAPIView.as_view(),name = "get_nfc_users"),#can both get and put new users with token
    path("meetings/",views.MeetingAPIView.as_view(),name = "get_meetings"),
    path("attendances/",views.AttendanceAPIView.as_view(),name = "get_attendance")
]