from . import db
from flask_login import UserMixin
from sql_alchemy.sql import func

class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(64), unique=True)
   email = db.Column(db.String(150), unique=True)
   password = db.Column(db.String(128))
   date_created = db.Column(db.Date(timezone=True), default=func.now())
