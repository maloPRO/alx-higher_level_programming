#!/usr/bin/python3
""" Lists all states that start with N """
import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    dtb = sys.argv[3]
    hst = "localhost"
    inpt = sys.argv[4]

    db = MySQLdb.connect(host=hst, user=usr, passwd=pwd, db=dtb, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \
            ORDER BY id".format(inpt))
    states = cur.fetchall()

    for state in states:
        print(state)
