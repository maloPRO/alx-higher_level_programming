#!/usr/bin/python3
""" Lists all states that start with N """
import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    dtb = sys.argv[3]
    hst = "localhost"

    db = MySQLdb.connect(host=hst, user=usr, passwd=pwd, db=dtb, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()

    for state in states:
        if ord(state[1][0]) == 78:
            print(state)
