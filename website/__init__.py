from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
   app = Flask(__name__)
   app.config['SECRET-KEY'] = 'secret'

   return app