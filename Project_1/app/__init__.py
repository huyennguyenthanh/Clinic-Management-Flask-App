from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
# from flask_login import LoginManager
# login = LoginManager(app)
# required user to lead to the login page
# login.login_view = 'login'
from app import routes
from app import models
from app import db
