#!/usr/bin/python3
"""
    Here the base model for state
    Here the code and rule
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class description of state"""
    __tablename__ = 'states'
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City") # type: ignore
