
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    id_favorites = Column(Integer, ForeignKey('favorites.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    id_planet = Column(Integer, ForeignKey('planets.id'))
    name_planet = Column(String(250), nullable=False)
    id_people = Column(Integer, ForeignKey('people.id'))
    name_people = Column(String(250), nullable=False)
    user = relationship(User)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name_people = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    favorites = relationship(Favorites)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name_planet = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    favorites = relationship(Favorites)

    def to_dict(self):
        return {}

# Dibujar el diagrama a partir de la base de datos de SQLAlchemy
render_er(Base, 'diagram.png')
## Draw from SQLAlchemy base
