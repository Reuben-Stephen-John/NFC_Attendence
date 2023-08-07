from backend import app,db
from backend.models import *
from backend.schemas import *
from flask import request,jsonify
from flask_migrate import upgrade
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_login import LoginManager, current_user,UserMixin,login_user,logout_user,login_required


login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@app.route('/',methods = ['GET'])
def home():
    routes = [
        '/get/users/all/',
        '/get/user/<string:serial>/',
        '/get/message/all/',
        '/get/attendances/all/',
        'mark/attendance/',
        '/login/'
    ]
    return jsonify(routes)
@app.route('/get/users/all/',methods = ['GET'])
def get_users():
    users = NFCUser.query.all()
    return nfc_user_schema.jsonify(users)
@app.route('/get/user/<string:serial>/',methods = ['GET'])
def get_user_with_nfc(serial):
    user = NFCUser.query.filter_by(nfc_serial = serial).first()
    return nfc_user_schema.jsonify(user,many=False)
@app.route('/get/meetings/all/',methods = ['GET'])
def get_meetings():
    meetings = Meeting.query.all()
    return meeting_schema.jsonify(meetings)
@app.route('/get/attendances/all/', methods=['GET'])
def get_attendances():
    attendances = Attendance.query.all()
    return attendance_schema.jsonify(attendances, many=True)
@app.route('/get/attendance/<string:serial>/',methods = ['GET'])
def get_attendance_with_nfc(serial):
    user = NFCUser.query.filter_by(nfc_serial=serial).first()
    attendances = Attendance.query.filter_by(user=user).all()
    return attendance_schema.jsonify(attendances)
@app.route('/mark/attendance/', methods=['POST'])
def create_attendance():
    data = request.get_json()
    try:
        attendance = Attendance.query.filter_by(meeting_id = data['meeting_id'],user_id = data['user_id']).first()
        attendance.status = data['status']
        attendance.date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
        db.session.commit()
    except:
        attendance = Attendance(meeting_id = data['meeting_id'],user_id = data['user_id'],status = data['status'],date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'))
        db.session.add(attendance)
        db.session.commit()
    return jsonify({'message': 'Attendance created successfully'})
    # except:
    #     return "Error Processing Request",400
@app.route('/migrate')
def migrate_database():
    with app.app_context():
        upgrade()
    return 'Database migration complete'
@app.route('/login/',methods = ['GET','POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    user_schema = UserSchema()
    if user and user.check_password(password):
        login_user(user)
        access_token = create_access_token(identity=user.id)
        return jsonify({'access_token': access_token,"user":user_schema.dump(user)})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
@app.route('/create/db')
def create_db():    
    db.create_all()
    return "",200
# Create a new route for user registration
@app.route('/register/', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # Check if the username is already taken
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    # Hash the password before storing it in the database
    hashed_password = generate_password_hash(password).decode('utf-8')

    # Create a new User object
    new_user = User(username=username, password=hashed_password, email=email)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201