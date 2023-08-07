from backend import ma
from backend.models import *

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id","username","email")
class NFCUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NFCUser
        
class MeetingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Meeting
        include_fk = True
class AttendanceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Attendance
        include_fk = True
user_schema = UserSchema(many = True)
nfc_user_schema = NFCUserSchema(many = True)
meeting_schema = MeetingSchema(many = True)
attendance_schema = AttendanceSchema(many = True)