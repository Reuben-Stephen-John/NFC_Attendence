import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS

SECRET_KEY = secrets.token_bytes(32)
JWT_SECRET_KEY=secrets.token_bytes(32)
app=Flask(__name__)
cors = CORS(app,resources={r"/api/*":{"origins":"*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",default = 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = SECRET_KEY
app.config['JWT_SECRET_KEY']=JWT_SECRET_KEY

#init db
db=SQLAlchemy(app)
migrate = Migrate(app,db)
#init ma
ma=Marshmallow(app)
jwt_manager = JWTManager(app)
from backend import models, views

if __name__ == '__main__':
    app.run(debug=True)

