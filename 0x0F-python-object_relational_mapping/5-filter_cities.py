#!/usr/bin/python3
"""
    The module file for the Exo 5
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
            sid = "SELECT id FROM states WHERE name = '%s'"
            query = "SELECT name FROM cities WHERE state_id = ({})".format(sid)
            cur.execute(query % (search))
            res = cur.fetchall()
            string = []
            for x in res:
                string.append(x[0])
            print(", ".join(string))
            db.close()
        except Exception as e:
            print("{}".format(e))
    else:
        print("Arguments are insufficient")
