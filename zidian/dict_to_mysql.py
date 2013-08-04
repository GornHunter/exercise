__author__ = 'nancy'

import MySQLdb

db = MySQLdb.connect(db="exercise5", user="root", host="localhost")
db.autocommit(True)
c = db.cursor()
c.execute("DROP TABLE IF EXISTS worddict")
c.execute("""CREATE TABLE worddict(id INT PRIMARY KEY AUTO_INCREMENT,
                                   name varchar(128) not null,
                                   meaning mediumtext)""")

SAVE_DICT = '/home/nancy/Downloads/worddictionary'
word = eval(open(SAVE_DICT, 'r').read())
print word.keys()[:10]


import json
for key, value in word.items():
    # str(value) => "abc"
    c.execute("insert into worddict(name, meaning) values (%s, %s)", (key, json.dumps(value)))
    #
    # id=key
    # c.execute("insert into worddict (id) values (%s)" % id)
    # for midkey, midvalue in value.items():
    #     if midvalue:
    #         query = "update worddict set %s ='%s'"
    #         c.execute(query % (midkey, midvalue))
    #         exa = value['example']
    #         for eachmeaning in value['examples']:
    #             for finalkey, finalvalue in exa:
    #                 if finalvalue:
    #                     lean = "update worddict set %s='%s'"
    #                     c.execute(lean % (finalkey, finalvalue))
c.close()
db.commit()
