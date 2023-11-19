#!/usr/bin/python3
"""
This module lists state based on user input
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
             FROM states \
             INNER JOIN cities \
             ON states.id = cities.state_id \
             ORDER BY cities.id"
    cur.execute(query)
    cities = cur.fetchall()
    for city in cities:
        print(city)
