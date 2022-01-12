#!/usr/bin/python3
"""Defines a City model that inherits from SQLAlchemy 
Base and links to the MySQL table cities."""

from sqlalchemy import String, Column, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Represents a city in the database MySQL table
    Attributes:
          id(str): the city's id
          name(sqlalchemy.String): the city's name
          state_id: the city's state id
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
