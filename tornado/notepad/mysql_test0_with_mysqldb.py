__author__ = 'nancy'

# -*- coding: utf-8 -*-

import MySQLdb as mdb  #we import the MySQLdb module
import sys

try:

# we connect the database.the connect() method has four parameters.the first patameter is
# the host,where the MySQL database is located.in our case it is a localhost,e.g.our com-
# puter.the second parameter is the database user name.it is followed by the user's account
# password.the finally parameter is the database name.

    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

# from the connection,we get the cursor object.the cursor is used to traverse the records from
# the result set.we call the execute() method of the cursor and execute the sql statement.

    cur = con.cursor()
    cur.execute('select version()')

# we fetch the data.since we retrieve only one record.

    ver = cur.fetchone()
    print 'Datebase version is %s' % ver

# We check for errors. This is important, since working with databases is error prone.

except mdb.Error, e:
    print 'Error %d:%s' % (e.args[0], e.args[1])
    sys.exit(1)

# In the final step, we release the resources.

finally:
    if con:
        con.close()

