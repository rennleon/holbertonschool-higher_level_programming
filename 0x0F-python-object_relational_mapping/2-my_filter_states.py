#!/usr/bin/python3
""" This file connects to a db and executes a query """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username, password, dbname, state = argv[1:]

    db = MySQLdb.connect(
        user=username,
        passwd=password,
        host='localhost',
        port=3306,
        db=dbname)

    sql = """
        SELECT *
        FROM states
        WHERE name = '{:s}'
        ORDER BY id ASC
    """.format(state)

    c = db.cursor()
    c.execute(sql)
    res = c.fetchall()
    [print(r) for r in res if r[1] == state]
    c.close()

    db.close()
