#!/usr/bin/python3

"""
Script that lists all cities
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cur = db.cursor()
    inpt = argv[4]

    query = "SELECT cities.name \
            FROM cities \
            JOIN states ON states.id = citites.state_id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id"
    cur.execute(query, (inpt,))

    cities = cur.fetchall()

    for city in cities:
        print(city)
