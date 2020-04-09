from flask import Flask
from config import Config
from flask_login import LoginManager
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)

#create a MongoClient Object with the ip address and name of database
myclient = MongoClient("mongodb://localhost:27017")

#create a db object from database named mydatabase
mydb = myclient["mydatabase"]

#create a collection to store documents named users
mycol = mydb["users"]

#create a user and insert into collection
#user1 = {"username": "aa", "password": "aa"}
#mycol.insert_one(user1)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import routes