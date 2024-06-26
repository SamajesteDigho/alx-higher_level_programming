#!/usr/bin/python3
"""
    The module file for the Exo 3
    Here we define the rules
"""
import sys
from MySQLdb import connect


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 4:
        user = args[1]
        password = args[2]
        db_name = args[3]
        host = 'localhost'
        port = 3306
        search = args[4]

        db = connect(host, user, password, db_name)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name = '%s'" % (search))
        res = cur.fetchall()
        for x in res:
            print("{}".format(x))
        db.close()
