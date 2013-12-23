__author__ = 'nancy'

from collections import namedtuple
import sqlite3

#make a basic link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes', 'title', 'url'])

#list of links to work with
links = [
    Link(0, 83495, 7385948568.0, 109, "Named tuples are especially useful for assigning field names t",
         "http://docs.python.org/dev/library/collections#collections.namedtuple"),
    Link(1, 436376, 346775.0, 1365, "n addition to the methods inherited from tuples",
         "http://203.208.46.145/#newwindow=1&q=namedtuple"),
    Link(2, 73455, 8445635.0, 5356, "Class method that makes a new instance from an existing sequence or iterable.",
         "http://www.baidu.com/s?ie=utf-8&bs=over+my+shoulder&f=8&rsv_bp=1&wd=validation&rsv_sug3=11&rsv_sug=0&rsv_sug1=10&rsv_sug4=287&inputT=5280"),
    Link(3, 7665, 56777.0, 634, "tance of the named tuple replacing specified fields with new",
         "http://docs.python.org/dev/library/collections#collections.namedtuple"),
    Link(4, 436376, 2633566.0, 254, "source code used to create the named tuple class. The source makes the n",
         "http://docs.python.org/dev/library/collections#collections.namedtuple"),
    Link(5, 7678534, 2542526.0, 545, "N tuple, use the double-star-operator (as describe",
         "http://docs.python.org/dev/library/collections#collections.namedtuple"),
    Link(6, 8495, 7477878.0, 4563, "regular Python class, it is easy to add or change functionalite",
         "http://docs.python.org/dev/library/collections#collections.namedtuple"),
    Link(7, 436376, 573442.0, 536, "This helps keep memory requirements low by preventing t",
         "http://http://www.bioon.com/biology/biomed/584874.shtml"),
    Link(12, 657878, 2256767.0, 785, "demented by using _replace() to customize a prototype instance",
         "http://docs.python.org/dev/library/collections#collections.namedtuple"),
    Link(13, 3577, 254556.0, 444, "sed constructor that is convenient for use cases where named tup",
         "http://docs.python.org/dev/library/collections#collections.namedtuple"),
    Link(14, 78256, 636537.0, 776, "insertion position is left unchanged. Deleting an entry and reinserting ",
         "http://http://www.bioon.com/biology/biomed/584875.shtml"),
    Link(15, 87323, 7655321.0, 776, " The item is moved to the right end if last is true",
         "http://http://developer.51cto.com/"),
    Link(16, 98876, 7462352.0, 857,
         " but they remember the order that items were inserted. When iterating over an ordered",
         "http://http://developer.51cto.com/art/201307/402696.htm"),
    Link(17, 24567, 67487784.0, 234, "it can be used in conjuction with sorting to make a sorted dictionary",
         "http://news.baidu.com/ns?cl=2&rn=20&tn=news&word=validation&ie=utf-8"),
]

#links is a list of link objects.links have a handful of properties.For
#example,a link's number of votes can be accessed by link.votes if "link"
#is a link.

#make the function query() return the number of votes for the link whose ID is 15

def query():
    for l in links:
        # print(l)
        if l.id == 15:
            return l.votes

# print(query())

#make the function query() return a list of links submitted by user 436376,by
#submission time ascending

def query_a():
    submissions = []
    for l in links:
        if l.submitter_id == 436376:
            submissions.append(l)
    submissions.sort(key=lambda x: x.submitted_time)
    return submissions

# print(query_a())

#make and populate a table

db = sqlite3.connect(':memory:')
db.execute('create table links'
           '(id integer,submitter_id integer,submitted_time integer,'
           'votes integer,title text,url text)')
for l in links:
    db.execute('insert into links values (?,?,?,?,?,?)', l)

# db is an in-memory sqlite database that can respond to sql queries using the execute() function.

#for example,if you run
# c=db.execute('select * from links')
#c will be a "cursor" to the results of that query.you can use the fetchmany()
#function on the cursor to convert that cursor into a list of results.these
#results won't be links;they'll be tuples,but they can be passed turned into a
#link.

def query_02():
    c = db.execute('select * from links')
    # c=db.execute('select title from links')
    results = c.fetchall()
    return results


def query_03():
    cursor = db.execute('select * from links')
    for link_tuple in cursor:
        print(link_tuple)
        link = Link(*link_tuple)
        print(link)
        print(link.votes)


def query_04():
    c = db.execute("select * from links")
    print(c.fetchone())
    link = Link(*c.fetchone())

    return link.votes


def query_05():
    cursor = db.execute('select * from links')
    for link_tuple in cursor:
        links = Link(*link_tuple)
        if links.id == 2:
            print(links.votes)

#Quiz-make the function query() return the number of votes the link whit ID=2 has
def query_06():
    c = db.execute('select * from links where id=2')
    link = Link(*c.fetchone())
    return link.votes

#quiz-make the function query() return the id of link that was submitted by user
#436376 and has >20000 votes.
def query_07():
    c = db.execute('select * from links where submitter_id=436376 and votes>=500')
    # print(c)
    for link_tuple in c:
        print(link_tuple)
        link = Link(*link_tuple)
        print(link.id)

#quiz-make the function query() return the ids of the links that were
#submitted by user 436376 sorted by submission time ascending

def query_08():
    results = []
    c = db.execute('select * from links where submitter_id=436376 order by submitted_time')
    for link_tuple in c:
        links = Link(*link_tuple)
        results.append(links.id)
    return results


def query_09():
    results = []
    c = db.execute('select id from links where submitter_id=436376 order by submitted_time')
    # return c.fetchall()
    results = [t[0] for t in c]
    return results

# quiz-implement the function link_by_id() that takes a link's ID and returns  the link inself.
#normall,receive data after searching the whole database
def link_by_id(link_id):
    for l in links:
        if l.id == link_id:
            return l

#quiz-implement the function build_link_index() that create a python dictionary
#the maps a link's ID to the link itself
def build_link_index():
    index = {}
    # print(links)
    for l in links:
        index[l.id] = l
    return index


link_index = build_link_index()
print(link_index)


def link_by_id(link_id):
    return link_index.get(link_id)

#quiz-implement the function add_new_link() that both adds a link to
#the "links" list and updates the link_index dictionary.

def add_new_link(link):
    links.append(link)
    link_index[link.id] = link


l = Link(50, 1, 1, 1, "title", "url")
add_new_link(l)

print(link_by_id(50))
print(links[-1])
print(link_by_id( ))

# print(query_02())
# query_03()
# print(query_04())
# query_05()
# print(query_06())
# print(query_07())
# query_07()
# print(query_08())
# print(query_09())

# print(link_by_id(4))
# print(build_link_index())
