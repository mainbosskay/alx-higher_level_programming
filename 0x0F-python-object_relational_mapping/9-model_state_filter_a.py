#!/usr/bin/python3
"""Lists of all State objects that contain letter a
from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        dbname = sys.argv[3]
        dburl = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
        dbengine = create_engine(dburl)
        Base.metadata.create_all(dbengine)
        dbsession = sessionmaker(bind=dbengine)()
        quryres = dbsession.query(State).order_by(State.id.asc()).filter(
                State.name.like('%a%')
        )
        for states in quryres:
            print(f'{states.id}: {states.name}')
