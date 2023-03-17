#!/usr/bin/python3
"""
City module
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128),nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
