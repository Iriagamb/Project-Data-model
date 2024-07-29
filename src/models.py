import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Register(base):
    __tablename__: 'register'
    id = Column(Integer,primary_key=True)
    email = Column(String (50), unique=True, nullable=False)
    name_user = Column(String(50))
    lastname_user = Column(String(50))
    password = Column(varchar (50))

class Login(base):
    __tablename__:'login'
    id = Column(Integer,primary_key=True)
    email = Column(String (50), unique=True,nullable=False)
    password = Column(varchar (50))

class Neighbor_Directory(base):
    __tablename__:'neighbor_directory'
    id = Column(Integer,primary_key=True)
    user_others = Column(Integer(50))
    detail = Column(Integer(50))

class Personal(base):
    __tablename__:'personal'
    id = Column(integer,primary_key=True)
    name_user = Column(string(50))
    last_name = Column(String(50))
    dept = Column(String(50))
    localshop = Column(string(50))

class Products(base):
    __tablename__:'products'
    id = Column(Integer,primary_key)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
