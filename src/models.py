import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250))
    email= Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'seguidores'
    id = Column(Integer, primary_key=True)  
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))
    id_seguidor = Column(Integer, ForeignKey('usuarios.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    url = Column(String(500), nullable=False)
    id_post = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    comentario = Column(String(300))
    id_user = Column(Integer, ForeignKey('usuario.id'))
    id_post = Column(Integer, ForeignKey('post.id')) 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
