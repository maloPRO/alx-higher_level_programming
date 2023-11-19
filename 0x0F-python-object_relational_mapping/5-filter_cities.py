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
    query = "SELECT cities.name \
             FROM states \
             INNER JOIN cities \
             ON states.id = cities.state_id \
             WHERE states.name = %s \
             ORDER BY cities.id"

    cur.execute(query, (sys.argv[4],))
    cities = cur.fetchall()

    city_names = [city[0] for city in cities]
    result = ", ".join(city_names)
    print(result)
