__author__ = 'nancy'

from collections import namedtuple
import sqlite3

Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'vote',
                           'title', 'url'])
# print Link._fields

links = [Link(0, 12345, 1524525, 3252, "ujjiarojiojojpw", "jipqitjuiiooit"),
         Link(1, 23456, 2849393, 2384, "29ajhlwtgjhjhkk", "iqpouti9putqio"),
         Link(2, 73849, 2389498, 8923, "uhjhaihi8utiuaa", "uiatuihgfhuiui"),
         Link(3, 28439, 2984983, 2894, "2hiuhaipuitquiu", "iqu8t9uq98uuu9"),
         Link(4, 74383, 9939845, 2194, "uhiapur9ipuqrui", "ji8a9ur8q9tyu7u"),
         Link(5, 73849, 4264833, 323256, "uhiapur9ipuqrui", "ji8a9ur8q9tyu7u"),
         Link(6, 22222, 34555, 4532, "uhiapur9ipuqrui", "ji8a9ur8q9tyu7u")
]

db = sqlite3.connect('/tmp/example.db')
try:
    db.execute('''
    create table links (
    id interger, summitter_id integer
    )
    ''')
except Exception as e:
    print e


links_from_db = db.execute('select * from links')
for l in links_from_db:
    print l, 'before'
print 'before------------------'

for l in links:
    for i in range(1000):
        db.execute('insert into links values(?, ?)', (l.id, l.submitter_id))
    db.commit()

links_from_db = db.execute('select * from links')
for l in links_from_db:
    print l


def query():
    for l in links:
        if l.id == 3:
            return l.vote


def query_sort():
    submit = []
    for l in links:
        if l.submitter_id == 73849:
            submit.append(l)
    submit.sort(key=lambda x: x.submitted_time)
    # print sorted(submit,key=lambda y: y.submitted_time)
    return submit


print query_sort()
# print query()



