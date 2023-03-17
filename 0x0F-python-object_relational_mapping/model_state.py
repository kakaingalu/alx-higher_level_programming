#!/usr/bin/python3
"""
 a python file that contains the class definition\
         of a State and an instance Base = \
         declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
creates an instance of the declarative_base class
"""
Base = declarative_base()


class State(Base):
    """
    State class definition

    Attributes:
        __tablename__(str_): The table name of the class
        id (int): The id of the class
        name (str)": The name of the class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
