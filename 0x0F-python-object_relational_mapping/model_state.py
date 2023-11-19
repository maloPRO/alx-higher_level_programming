#!/usr/bin/python3

"""
This module contains class State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
