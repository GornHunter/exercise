__author__ = 'nancy'

import MySQLdb


# db = MySQLdb.connect(db="test", user="feng", host="192.168.1.101")
db = MySQLdb.connect(db="test2", user="root", host="localhost")
db.autocommit(True)
c = db.cursor()

cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS Writers")
cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
cur.execute("INSERT IN TO Writers(Name) VALUES('Emile Zola')")
cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
cur.execute("INSERT INTO Writers(Name) VALUES('Terry Pratchett')")

cur.execute("select * from Writers")
rows = cur.fetchall()
for r in rows:
    print r

cur.close()
db.commit()


# c.execute('select * from mysql.user')
# rows = c.fetchall()
# for r in rows:
#     print r

mydict = {'1': [{'First': 'John', 'Last': 'Doe'}, {'Company': 'Trulia Inc.', 'Title': 'CEO', 'YearsattheCompany': 4},
                {'Cell': '216-453-4322', 'Home': None}]}

for key, value in mydict.items():
    id = key
    print c.execute("insert into deldictmysql (id) values (%s)" % id)

    for eachdict in value:
        # print eachdict
        for finalkey, finalvalue in eachdict.items():
            # print finalkey, finalvalue
            if finalvalue:
                query = "update deldictmysql set %s = '%s'"
                # print query % (finalkey, finalvalue)
                c.execute(query % (finalkey, finalvalue))

c.close()
# db.commit()

