#!/usr/bin/python3
'''                                                                                                                                  a script that lists all states                                                                                                       from the database hbtn_0e_0_usa                                                                                                      '''
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    for x in c.fetchall():
        print(x)
    c.close()
    db.close()
