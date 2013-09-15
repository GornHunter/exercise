__author__ = 'nancy'

# -*- coding: utf-8 -*-

import MySQLdb as mdb


def read_image():

    fin = open("a0.png")
    img = fin.read()

    return img

def writeImage(data):

    fout = open('a0.png', 'wb')

    with fout:

        fout.write(data)

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')

with con:

    cur = con.cursor()
    data = read_image()
    cur.execute("INSERT INTO images VALUES(1, %s)", (data, ))

    cur.execute("SELECT Data FROM images WHERE Id=1")
    d = cur.fetchone()[0]
    writeImage(d)
