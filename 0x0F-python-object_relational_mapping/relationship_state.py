#!/usr/bin/python3
"""This module defines the State class for database interaction.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state in the 'states' table of the database.

    Args:
    id (int): An auto-generated, unique integer, primary key.
    name (str): A string with a maximum length of 128 characters.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
