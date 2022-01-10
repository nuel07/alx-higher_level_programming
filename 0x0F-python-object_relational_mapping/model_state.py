#!/usr/bin/python3
'''
Defines state model
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class State(Base):
    """
Represents a state in a MySQL database
Attributes:
    __tablename__(str): the name of the MySQL table
    id(sqlalchemy.Integer): the state's id
    name(sqlalchemy.String): the state's name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    
