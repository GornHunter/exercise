__author__ = 'nancy'

# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")




#------------the first output method----------------
    # cur.execute("SELECT * FROM Writers")
    # rows = cur.fetchall()
    #
    # for row in rows:
    #     print row

#-------------the second output method---------------
    # cur.execute("SELECT * FROM Writers")
    # print cur.rowcount
    # for i in range(cur.rowcount):
    #
    #     row = cur.fetchone()
    #     # print row
    #     print row[0], row[1]

# Column headers
# cur.execute("SELECT * FROM Writers LIMIT 5")
#
# rows = cur.fetchall()
#
# desc = cur.description
#
# print "%s %3s" % (desc[0][0], desc[1][0])
#
# for row in rows:
#     print "%2s %3s" % row

