#!/usr/bin/python3
import MySQLdb
import sys

mydb = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = mydb.cursor()

cur.execute('SELECT * FROM states ORDER BY id')

states = cur.fetchall()

for state in states:
    print(state)
