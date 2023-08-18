#!/usr/bin/python3

"""
Contains a script that lists all states
"""
import MySQLdb
import sys

mydb = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

cur = mydb.cursor()

cur.execute('SELECT * FROM states ORDER BY id')

states = cur.fetchall()

if __name__ == "__main__":
    for state in states:
        print(state)
