from flask import Flask
from config import Config
from flask_login import LoginManager
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import database
from app import routes