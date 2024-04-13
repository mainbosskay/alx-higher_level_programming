#!/usr/bin/python3
"""List of all states with name starting with N (upper N)
from database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        dbconnct = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
        )
        dbcurrt = dbconnct.cursor()
        dbquery = (
            'SELECT * FROM states WHERE name IS NOT NULL AND' +
            ' LEFT(CAST(name AS BINARY), 1) = "N" ORDER BY states.id ASC;'
        )
        dbcurrt.execute(dbquery)
        quryres = dbcurrt.fetchall()
        for row in quryres:
            print(row)
        dbconnct.close()
