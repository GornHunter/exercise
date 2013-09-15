__author__ = 'nancy'

# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

with con:
    # the default cursor returns the data in a tuple of tuples.when we use a dictionary
    # cursor,the data is sent in a form of python dictionaries.this way we can refer to the
    # data by their column names.

    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Writers LIMIT 4")

    rows = cur.fetchall()

    for row in rows:
        print row["Id"], row["Name"]

