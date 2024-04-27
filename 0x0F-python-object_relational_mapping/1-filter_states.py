#!/usr/bin/python3
"""
    The module file for the Exo 1
    Here we define the rules
"""
import sys
import MySQLdb


args = sys.argv
if len(args) > 3:
    user = args[1]
    password = args[2]
    db_name = args[3]
    host = 'localhost'
    port = 3306

    try:
        db = MySQLdb.connect(host, user, password, db_name)
        cur = db.cursor()
        cur.execute("SELECT * FROM states")
        res = cur.fetchall()
        for x in res:
            if x[1][0] == 'N':
                print("{}".format(x))
        db.close()
    except Exception as e:
        print("{}".format(e))
else:
    print("Arguments are insufficient")
