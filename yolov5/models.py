from flask import Flask
from app import db



class User(db.Model):
    user_seq = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(200), unique=True, nullable=True)
    password = db.Column(db.String(200), nullable=False)
    re_password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable = False)
    phone = db.Column(db.String(150), unique=True, nullable = False)
    age = db.Column(db.Integer(8), nullable = False)
    sex = db.Column(db.String(2), nullable = False)
    height = db.Column(db.Float(150), unique=True, nullable = False)
    weight = db.Column(db.Float(150), unique=True, nullable = False)