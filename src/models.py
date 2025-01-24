import os
import sys
from sqlalchemy import ForeignKey, Integer, String
from eralchemy2 import render_er
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import enum

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(100))

class Follower(db.Model):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)

class Comment(db.Model):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    comment_text = db.Column(db.String(250))
    author_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)

    def to_dict(self):
        return {}
    
class Post(db.Model):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True, index=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {}


class MediaType(enum.Enum):
    TYPE = "PNG"

class Media(db.Model):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True, index=True, nullable=False)
    type = db.Column(db.Enum(MediaType), unique=True, nullable=False)
    url = db.Column(db.String(250), nullable=False, unique=True)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e