#!/usr/bin/python3
"""Lists of all cities from the database hbtn_0e_4_usa"""
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
            'SELECT cities.id, cities.name, states.name FROM cities ' +
            'INNER JOIN states ON cities.state_id = states.id ' +
            'ORDER BY cities.id ASC;'
        )
        dbcurrt.execute(dbquery)
        quryres = dbcurrt.fetchall()
        for row in quryres:
            print(row)
        dbconnct.close()
