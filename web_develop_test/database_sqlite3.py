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

# db = sqlite3.connect(':memory:')
db = sqlite3.connect('/tmp/example.db')
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
    c = db.execute("select * from links where id=2")
    link = Link(*c.fetchone())
    return link.vote


def query_1():
    c = db.execute("select * from links where submitter_id=74383 and vote>1000")
    link = Link(*c.fetchone())
    return link.id


def query_orderby():
    results = []
    c = db.execute("select * from links where submitter_id=73849 order by submitted_time")
    for link_tuple in c:
        link = Link(*link_tuple)
        results.append(link.id)
    return results


def query_order_another():
    c = db.execute("select id from links where submitter_id=73849 order by submitted_time asc")
    results = [t[0] for t in c]
    return results


def link_by_id(link_id):
    for l in links:
        if l.id == link_id:
            return l


def build_link_index():
    index = {}
    for l in links:
        index[l.id] = l
    return index


link_index = build_link_index()


def link_id(link_id):
    return link_index[link_id]


def add_new_link(l):
    links.append(l)
    link_index[l.id] = l


l = Link(50, 1, 1, 1, 'title', 'url')
add_new_link(l)
print links[-1]
print link_id(50)

print link_id(3), '*******'

print build_link_index()
print link_by_id(5)

print query_1(), '------'
print query_orderby()
print query_order_another(), '2222'

query()

print query()


class HashTable(object):
    def __init__(self):
        self.array = [None] * 10
        self.hash_func = id

    def get(self, key):
        idx = self.hash_func(key) % len(self.array)
        while 1:
            item = self.array[idx % len(self.array)]
            if item:
                i_key, i_value = item
                if i_key == key:
                    return i_value
                else:
                    idx += 1
            else:
                return None


    def set(self, key, value):
        idx = self.hash_func(key) % len(self.array)
        while 1:
            if self.array[idx] is None:
                self.array[idx] = (key, value)
                return
            else:
                old_key, old_value = self.array[idx]
                if old_key == key:
                    self.array[idx] = (key, value)
                    return
                # TODO resize hash table, reinsert all the exist key & value, then reinsert key&value
                idx = (idx + 1) % len(self.array)


def test_hash_table():
    ht = HashTable()
    ht.set("100", 1)

    ht.set("100", 2)

    ht.set("120", 3)

    print ht.get("111")
    print ht.get("100")


print test_hash_table()