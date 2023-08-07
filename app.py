from backend import app,db
from backend.models import *
from flask_login import LoginManager, current_user,UserMixin,login_user,logout_user,login_required
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
class MyModelView(ModelView):
    column_hide_backrefs = False
    column_display_pk = True
    decorators = [login_required] 

class MyModelView(ModelView):
    column_hide_backrefs = False
    column_display_pk = True
    decorators = [login_required] 
class MyAttendanceModelView(ModelView):
    column_list = ['meeting', 'user', 'status', 'date']
    decorators = [login_required] 
admin = Admin(app)
admin._menu = admin._menu[1:]
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(NFCUser,db.session))
admin.add_view(MyModelView(Meeting, db.session))
admin.add_view(MyAttendanceModelView(Attendance, db.session))
    
if __name__ == '__main__':
   
    app.run()