#!/usr/bin/python3
"""
This script defines a City class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """State class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'))
