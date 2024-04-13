#!/usr/bin/python3
"""Creating the State “California” with the City “San Francisco"
from the database hbtn_0e_100_usa"""
import sys
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        user = sys.argv[1]
        passwd = sys.argv[2]
        dbname = sys.argv[3]
        dburl = f"mysql://{user}:{passwd}@localhost:3306/{dbname}"
        dbengine = create_engine(dburl)
        Base.metadata.create_all(dbengine)
        dbsession = sessionmaker(bind=dbengine)()
        nwstate = State(name='California')
        nwcity = City(name='San Francisco')
        nwstate.cities.append(nwcity)
        dbsession.add(nwstate)
        dbsession.commit()
