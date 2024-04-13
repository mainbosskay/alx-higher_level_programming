#!/usr/bin/python3
"""Lists of all City objects from the database hbtn_0e_101_usa"""
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
        quryres = dbsession.query(City).join(State).order_by(City.id.asc())
        for cty in quryres.all():
            print(f"{cty.id}: {cty.name} -> {cty.state.name}")
