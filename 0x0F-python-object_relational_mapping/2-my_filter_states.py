#!/usr/bin/python3
"""Argument and display values in states table of hbtn_0e_0_usa
where name matches the argument"""
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
            'SELECT * FROM states WHERE CAST(name AS BINARY) LIKE ' +
            'CAST("{}" AS BINARY) ORDER BY id ASC;'.format(statenm)
        )
        dbcurrt.execute(dbquery)
        quryres = dbcurrt.fetchall()
        for row in quryres:
            print(row)
        dbconnct.close()
