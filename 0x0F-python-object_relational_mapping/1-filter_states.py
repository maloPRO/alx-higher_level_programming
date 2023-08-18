#!/usr/bin/python3

"""
This script listts all states starting with N
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

    cur.execute('Select * FROM states ORDER BY id')

    states = cur.fetchall()

    for state in states:
        if ord(state[1][0]) == 78:
            print(state)
