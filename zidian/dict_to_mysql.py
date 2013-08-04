__author__ = 'nancy'

import MySQLdb

db = MySQLdb.connect(db="exercise5", user="root", host="localhost")
db.autocommit(True)
c = db.cursor()
c.execute("DROP TABLE IF EXISTS WORDDICT")
c.execute("CREATE TABLE WORDDICT(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")

SAVE_DICT = '/home/nancy/Downloads/worddictionary'
word = eval(open(SAVE_DICT, 'r').read())
print word

for key, value in word.items():
    id=key
    c.execute("insert into WORDDICT (id) values (%s)" % id)
    for midkey, midvalue in value.items():
        if midvalue:
            query = "update WORDDICT set %s ='%s'"
            c.execute(query % (midkey, midvalue))
            exa = value['example']
            for eachmeaning in value['examples']:
                for finalkey, finalvalue in exa:
                    if finalvalue:
                        lean = "update WORDDICT set %s='%s'"
                        c.execute(lean % (finalkey, finalvalue))
c.close()
db.commit()
