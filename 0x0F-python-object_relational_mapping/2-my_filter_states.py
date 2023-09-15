#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
"""
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    mycursor = db.cursor()
    sql_query = """
    SELECT *
    FROM states
    WHERE name = %s
    ORDER BY id ASC
    """
    mycursor.execute("""
    SELECT *
    FROM states
    WHERE name LIKE BINARY '{}'
    ORDER BY id ASC
    """.format(state_name))
    states = mycursor.fetchall()

    for state in states:
        print(state)

    mycursor.close()
    db.close()
