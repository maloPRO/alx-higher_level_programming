#!/usr/bin/python3

import MySQLdb
import sys

usr, pwd, hst, prt, dbase = sys.argv[1], sys.argv[2], "localhost", 3306, sys.argv[3]
if __name__ == "__main__":
    db = MySQLdb.connect(host=hst,
                         port=prt,
                         user=usr,
                         passwd=pwd,
                         db=dbase)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    states = cur.fetchall()

    for state in states:
        print(state)
