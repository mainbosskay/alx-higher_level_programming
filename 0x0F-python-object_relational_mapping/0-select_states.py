#!/usr/bin/python3
"""Python script that lists all states from the database hbtn_0e_0_usa"""
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
        dbquery = "SELECT * FROM states ORDER BY id ASC;"
        dbcurrt.execute(dbquery)
        quryres = dbcurrt.fetchall()
        for row in quryres:
            print(row)
        dbconnct.close()
