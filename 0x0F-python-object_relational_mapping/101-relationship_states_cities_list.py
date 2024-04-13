#!/usr/bin/python3
"""Listing all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        dbname = sys.argv[3]
        dburl = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
        dbengine = create_engine(dburl)
        Base.metadata.create_all(dbengine)
        dbsession = sessionmaker(bind=dbengine)()
        quryres = dbsession.query(State).order_by(State.id.asc()).all()
        for states in quryres:
            print(f"{states.id}: {states.name}")
            for cty in states.cities:
                print(f"\t{cty.id}: {cty.name}")
        dbsession.close()
