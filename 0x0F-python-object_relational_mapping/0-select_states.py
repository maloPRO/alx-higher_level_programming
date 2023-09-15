#!/usr/bin/python3
""" Lists all states """
import MySQLdb
import sys

usr = sys.argv[1]
pwd = sys.argv[2]
dtb = sys.argv[3]
hst = "localhost"

if __name__ == "__main__":
    db = MySQLdb.connect(host=hst, user=usr, passwd=pwd, db=dtb, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()
    
    for state in states:
        print(state)
