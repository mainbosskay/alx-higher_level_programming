#!/usr/bin/python3
"""Module is created to define the state model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
"""Standardized structure is utilized to represent base class for all tables"""


class State(Base):
    """Class represents a state retrieved from the states table"""
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
