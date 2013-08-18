__author__ = 'nancy'

from collections import namedtuple
import sqlite3

Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'vote',
                           'title', 'url'])

links = [Link(0, 12345, 1524525, 3252, "ujjiarojiojojpw", "jipqitjuiiooit"),
         Link(1, 23456, 2849393, 2384, "29ajhlwtgjhjhkk", "iqpouti9putqio"),
         Link(2, 73849, 2389498, 8923, "uhjhaihi8utiuaa", "uiatuihgfhuiui"),
         Link(3, 28439, 2984983, 2894, "2hiuhaipuitquiu", "iqu8t9uq98uuu9"),
         Link(4, 74383, 9939845, 2194, "uhiapur9ipuqrui", "ji8a9ur8q9tyu7u"),
         Link(5, 73849, 4264833, 323256, "uhiapur9ipuqrui", "ji8a9ur8q9tyu7u"),
         Link(6, 22222, 34555, 4532, "uhiapur9ipuqrui", "ji8a9ur8q9tyu7u")]

db = sqlite3.connect(':memory:')
db.execute('create table links (id integer,submitter_id integer,submitted_time integer,'
           'vote integer,title text,url text)')
for l in links:
    db.execute('insert into links values (?,?,?,?,?,?)', l)
    db.commit()


def query():
    # c = db.execute("select * from links")
    # c=db.execute("select title from links"
    # results = c.fetchall()
    cursor = db.execute("select * from links")
    for link_tuple in cursor:
        # print link_tuple
        link = Link(*link_tuple)
        # return results
        # print link.vote
    c=db.execute("select * from links where id=2")
    link=Link(*c.fetchone())
    return link.vote


query()

print query()