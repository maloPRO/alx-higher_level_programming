#!/usr/bin/python3

"""
This module contains class State
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    city class
    """
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
