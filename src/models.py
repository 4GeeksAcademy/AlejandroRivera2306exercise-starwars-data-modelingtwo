
# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy import create_engine
# from eralchemy2 import render_er


# Base = declarative_base()

# class Personaje(Base):
#     __tablename__ = 'personaje'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     birth_year = Column(String(250), nullable=False)
#     gender = Column(String(250), nullable=False)
#     # favorito = relationship(Favorito)

# class Planeta(Base):
#     __tablename__ = 'planeta'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     terrain = Column(String(250), nullable=False)
#     climate = Column(String(250), nullable=False)
#     # favorito = relationship(Favorito)
# class Usuario(Base):
#     __tablename__ = 'usuario'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     email = Column(String(250), nullable=False)
#     password = Column(String(250), nullable=False)
    

# class Favorito(Base):
#     __tablename__ = 'favorito'
#     id = Column(Integer, primary_key=True)
#     id_planeta = Column(Integer, ForeignKey('planeta.id'))
#     name_planeta = Column(String(250), nullable=False)
#     id_personaje = Column(Integer, ForeignKey('personaje.id'))
#     name_personaje = Column(String(250), nullable=False)
#     id_favorito = Column(Integer, ForeignKey('usuario.id'))
    







#     def to_dict(self):
#         return {}

# # Dibujar el diagrama a partir de la base de datos de SQLAlchemy
# render_er(Base, 'diagram.png')
# ## Draw from SQLAlchemy base

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", back_populates="personaje")

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", back_populates="planeta")

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favoritos = relationship("Favorito", back_populates="usuario")

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    id_planeta = Column(Integer, ForeignKey('planeta.id'))
    name_planeta = Column(String(250), ForeignKey('planeta.name'), nullable=False)
    id_personaje = Column(Integer, ForeignKey('personaje.id'))
    name_personaje = Column(String(250), ForeignKey('personaje.name'), nullable=False)
    id_favorito = Column(Integer, ForeignKey('usuario.id'))
    planeta = relationship("Planeta", back_populates="favoritos")
    personaje = relationship("Personaje", back_populates="favoritos")
    usuario = relationship("Usuario", back_populates="favoritos")

    def to_dict(self):
        return {}

# Dibujar el diagrama a partir de la base de datos de SQLAlchemy
render_er(Base, 'diagram.png')
