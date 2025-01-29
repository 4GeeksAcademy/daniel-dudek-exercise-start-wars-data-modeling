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

class Species(db.Model):
    __tablename__ = 'species'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = db.Column(db.Integer, primary_key=True, unique=True, index=True, nullable=False)
    description = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    homeworld = db.Column(db.Integer, ForeignKey('planets.uid'), nullable=False)
    email = db.Column(db.String(100))

class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = db.Column(db.Integer, primary_key=True, unique=True, index=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    gravity = db.Column(db.String(100), nullable=False)

class People(db.Model):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = db.Column(db.Integer, primary_key=True, unique=True, index=True, nullable=False)
    description = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    homeworld = db.Column(db.Integer, ForeignKey('planets.uid'), nullable=False)
    
class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, nullable=False)

class FavoritesType(enum.Enum):
    SPECIES = "SPECIES"
    PLANETS = "PLANETS"
    PEOPLE = "PEOPLE"

class Favorites(db.Model):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'),index=True, nullable=False)
    external_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Enum(FavoritesType), nullable=False)
    name = db.Column(db.String(30), nullable=False)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
