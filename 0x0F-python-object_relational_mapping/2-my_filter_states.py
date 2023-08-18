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

    state_name = sys.argv[4]
    cur = mydb.cursor()
    cur.execute('SELECT * FROM states WHERE name = (%s) ORDER BY id',
                (state_name,))
    states = cur.fetchall()

    for state in states:
        print(state)
