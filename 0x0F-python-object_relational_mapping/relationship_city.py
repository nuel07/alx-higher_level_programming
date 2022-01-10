#!/usr/bin/python3
'''
Defines City model
'''
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

class City(Base):
    '''
    Represents an improved City class
Attributes:
    id: the city's id
    name: the city's name
    state_id: the city's state id
   '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    
