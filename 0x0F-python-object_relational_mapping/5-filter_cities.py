#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        dbconnct = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
        )
        dbcurrt = dbconnct.cursor()
        statenm = sys.argv[4]
        dbquery = (
            'SELECT cities.name FROM cities ' +
            'INNER JOIN states ON cities.state_id = states.id ' +
            'WHERE CAST(states.name AS BINARY) = %s ' +
            'ORDER BY cities.id ASC;'
        )
        dbcurrt.execute(dbquery, (statenm,))
        quryres = dbcurrt.fetchall()
        print(', '.join(map(lambda cty: cty[0], quryres)))
        dbconnct.close()
