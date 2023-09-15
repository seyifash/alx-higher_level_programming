#!/usr/bin/python3
"""
This script takes the name of a state as an argument
and lists all cities of that state
from the 'hbtn_0e_4_usa' database using MySQLdb.
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
sql_query = '''
SELECT cities.id, cities.name
FROM cities INNER JOIN states ON cities.state_id = states.id
WHERE states.name = %s
ORDER BY cities.id ASC
'''
mycursor.execute(sql_query, (state_name,))
cities = [row[1] for row in mycursor.fetchall()]

mycursor.close()
db.close()

city_names = ", ".join(cities)
print(city_names)
