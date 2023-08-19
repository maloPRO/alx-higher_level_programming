#!/usr/bin/python3

"""
prints state based on usser input
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    cur = mydb.cursor()
    inpt = sys.argv[4]

    query = "SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \
            ORDER BY id".format(inpt)

    cur.execute(query)

    states = cur.fetchall()

    for state in states:
        print(state)
