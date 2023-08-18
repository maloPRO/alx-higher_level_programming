#!/usr/bin/python3

"""
prints state based on usser input
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mydb = MySQLdb.connect(host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])

    cur = mydb.cursor()

    query = 'SELECT * FROM states ORDER BY id'
    cur.execute(query)
    inpt = sys.argv[4]
    states = cur.fetchall()

    for state in states:
        if state[1] == inpt:
            print(state)
