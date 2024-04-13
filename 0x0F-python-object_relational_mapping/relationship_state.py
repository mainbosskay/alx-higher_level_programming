#!/usr/bin/python3
"""Module has been created to define the State model"""
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
"""Common structure is used to represent the base class for all tables"""


class State(Base):
    """This class encapsulates state entity retrieved from states table"""
    __tablename__ = "states"
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
    cities = relationship(
            "City",
            cascade="all, delete, delete-orphan",
            backref="state"
    )
