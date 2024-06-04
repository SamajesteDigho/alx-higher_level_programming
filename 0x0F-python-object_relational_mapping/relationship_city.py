#!/usr/bin/python3
"""
    Here the base model for city
    Here the code and rule
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import State

Base = declarative_base()


class City(Base):
    """Here the class definition of cities"""
    __tablename__ = 'cities'
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey("states.id"))
    # state: Mapped["State"] = relationship(back_populates="cities")
