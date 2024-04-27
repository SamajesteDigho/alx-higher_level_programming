#!/usr/bin/python3
"""
    The module file for the Exo 4
    Here we define the rules
"""
import sys
import MySQLdb


if __name__ == '__main__':
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
            query = "SELECT ct.id, ct.name, st.name FROM cities ct, states st WHERE st.id = ct.state_id"
            cur.execute(query)
            res = cur.fetchall()
            for x in res:
                print("{}".format(x))
            db.close()
        except Exception as e:
            print("{}".format(e))
    else:
        print("Arguments are insufficient")
