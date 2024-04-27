#!/usr/bin/python3
"""
    The module file for the Exo 2
    Here we define the rules
"""
import sys
import MySQLdb


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 4:
        user = args[1]
        password = args[2]
        db_name = args[3]
        host = 'localhost'
        port = 3306
        search = args[4]

        try:
            db = MySQLdb.connect(host, user, password, db_name)
            cur = db.cursor()
            cur.execute("SELECT * FROM states WHERE name = '%s'" % (search))
            res = cur.fetchall()
            for x in res:
                print("{}".format(x))
            db.close()
        except Exception as e:
            print("{}".format(e.__traceback__()))
    else:
        print("Arguments are insufficient")
