#!/usr/bin/python3
"""script that lists all states with a name starting with N
"""
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    mycursor = db.cursor()
    mycursor.execute("""
            SELECT *
            FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY id ASC
        """)
    states = mycursor.fetchall()

    for state in states:
        print(state)

    mycursor.close()
    db.close()
