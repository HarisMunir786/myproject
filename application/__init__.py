from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from os import getenv

app = Flask(__name__)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass123@35.246.85.220/pojectdb'
db = SQLAlchemy(app)

from application import routes
