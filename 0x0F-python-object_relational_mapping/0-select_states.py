#!/usr/bin/python3
""" Lists all states """
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id")
states = cur.fetchall()
for state in states:
    print(state)
