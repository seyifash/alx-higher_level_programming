#!/usr/bin/python3
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
sql_query = '''
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC
'''
mycursor.execute(sql_query)
states = mycursor.fetchall()

for state in states:
    print(state)

mycursor.close()
db.close()
