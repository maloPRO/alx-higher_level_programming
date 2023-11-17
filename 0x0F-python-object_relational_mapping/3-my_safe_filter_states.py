#!/usr/bin/python3
"""
This module lists state based on user input
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states \
             WHERE name LIKE BINARY '{}%' \
             ORDER BY states.id".format(sys.argv[4])
    cur.execute(query)

    states = cur.fetchall()
    for state in states:
        print(state)
