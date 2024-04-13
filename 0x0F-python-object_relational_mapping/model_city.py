#!/usr/bin/python3
"""Module is established to contain the City model"""
from model_state import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """Class represents a row from the cities table"""
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
    state = relationship('State', backref='cities')
