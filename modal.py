from flask_login import UserMixin
from app import db 
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))