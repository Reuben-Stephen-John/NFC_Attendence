from datetime import datetime
from backend import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(1000),nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self,username,email,password):
        self.username  = username
        self.email=email
        self.set_password(password)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def get_id(self):
        return self.id
    def __repr__(self):
        return self.username

class NFCUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(1000),nullable = False)
    nfc_serial = db.Column(db.String(100),unique = True, nullable = False)
    roll_no = db.Column(db.String(100),nullable = False)
    faculty_registered = db.Column(db.String(200),nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def get_id(self):
        return str(self.id)
    def __repr__(self):
        return self.username
class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(1000),nullable = False)
    created_at = db.Column(db.DateTime)
    
    def __repr__(self):
        return self.name
    
VALID_STATUSES = ['Present', 'Absent', 'On-Duty']
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('nfc_user.id'), nullable=False)
    status = db.Column(db.String(100),nullable=False)
    date = db.Column(db.DateTime)
    meeting = db.relationship('Meeting', backref=db.backref('attendances', lazy='dynamic'))
    nfcuser = db.relationship('NFCUser', backref=db.backref('attendances', lazy='dynamic'))

    def __init__(self, meeting_id, user_id, status, date=datetime.utcnow):
        if status not in VALID_STATUSES:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(VALID_STATUSES)}")
        self.meeting_id = meeting_id
        self.user_id = user_id
        self.status = status
        self.date = date