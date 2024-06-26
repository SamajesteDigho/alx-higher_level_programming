#!/usr/bin/python3
"""
    Here the base model for city
    Here the code and rule
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Here the class definition of cities"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __init__(self, name, state_id):
        """Here the initialization"""
        self.name = name
        self.state_id = state_id
