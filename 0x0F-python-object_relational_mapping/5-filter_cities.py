#!/usr/bin/python3
"""
 a script that lists all states with a name starting \
         with N (upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Get data from database
    """

    db_conct = MySQLdb.connect(host="localhost", user=argv[1],
                               port=3306, passwd=argv[2],
                               db=argv[3], charset="utf8")

    cursor = db_conct.cursor()
    query = "SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name ='{}' ORDER BY cities.id ASC".format(argv[4])
    cursor.execute(query)

    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    db_conct.close()
