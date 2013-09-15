__author__ = 'nancy'

# -*- coding: utf-8 -*-
# prepared statements
import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')



with con:

    cur = con.cursor()

    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s",
                ("limeei", "1"))

    a=cur.rowcount
    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s",
                ("yangryi", "2"))
    a=a+cur.rowcount
    print "Number of rows updated:",  a
    print cur.rowcount
