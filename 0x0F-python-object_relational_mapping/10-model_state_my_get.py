#!/usr/bin/python3
"""Printing the State object with the name passed as argument
from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        user = sys.argv[1]
        passwd = sys.argv[2]
        dbname = sys.argv[3]
        statenm = sys.argv[4]
        vchr = map(lambda ch: ch.isalpha() or (ch in (' ', '%', '_')), statenm)
        if not all(vchr):
            statenm = ''
        dburl = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
        dbengine = create_engine(dburl)
        Base.metadata.create_all(dbengine)
        dbsession = sessionmaker(bind=dbengine)()
        quryres = dbsession.query(State).filter(State.name == statenm).first()
        if quryres is None:
            print("Not found")
        else:
            print(f"{quryres.id}")
