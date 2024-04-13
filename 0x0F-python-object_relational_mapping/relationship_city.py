#!/usr/bin/python3
"""Module is created to define the City model"""
from relationship_state import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """Class represents a record from the cities table"""
    __tablename__ = "cities"
    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
    )
    name = Column(
            String(length=128),
            nullable=False
    )
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False
    )
