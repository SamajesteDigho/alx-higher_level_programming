#!/usr/bin/python3
"""
    The module file for the Exo 4
    Here we define the rules
"""
import sys
from MySQLdb import connect


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 3:
        user = args[1]
        password = args[2]
        db_name = args[3]
        host = 'localhost'
        port = 3306

        db = connect(host, user, password, db_name)
        cur = db.cursor()
        cur.execute("SELECT ct.id, ct.name, st.name "
                    + "FROM cities ct, states st "
                    + "WHERE st.id = ct.state_id")
        res = cur.fetchall()
        for x in res:
            print("{}".format(x))
        db.close()
