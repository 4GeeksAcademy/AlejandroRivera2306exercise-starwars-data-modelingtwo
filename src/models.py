
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
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Integer, nullable=False)
    favoritos = relationship("Favorito")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    id_planeta = Column(Integer, ForeignKey('planeta.id'))
    name_planeta = Column(String(250), nullable=False)
    id_personaje = Column(Integer, ForeignKey('personaje.id'))
    name_personaje = Column(String(250), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id'))
    planeta = relationship("Planeta", foreign_keys=[id_planeta])
    personaje = relationship("Personaje", foreign_keys=[id_personaje])
    user = relationship("User")

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", foreign_keys=[Favorito.id_personaje])

  

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", foreign_keys=[Favorito.id_planeta])


# Dibujar el diagrama a partir de la base de datos de SQLAlchemy
render_er(Base, 'diagram.png')
