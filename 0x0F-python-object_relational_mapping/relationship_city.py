#!/usr/bin/python3
""" model_city.py that contains the class definition of a City.
"""

import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm  import relationship
from relationship_state import Base

class City(Base):
    """
    Represents a state in the 'states' table of the database.

    Args:
    id (int): An auto-generated, unique integer, primary key.
    name (str): A string with a maximum length of 128 characters.
    state_id (int): An integer representing the foreign key relationship
    to the 'states' table.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state_relation = relationship("State", overlaps="cities,state")
