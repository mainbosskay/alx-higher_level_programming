#!/usr/bin/python3
"""Printing all City objects from the database hbtn_0e_14_usa"""
import sys
from model_city import City
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
        quryres = dbsession.query(City).order_by(City.id.asc()).all()
        for row in quryres:
            print(f"{row.state.name}: ({row.id}) {row.name}")
