__author__ = 'Nancy'

import re
# match=re.search('iig','called piiig')
# print(match)
#
# print(match.group())

def Find(pat,text):
    match=re.search(pat,text)
    if match:
        print(match.group())
    else:
        print('not found')

Find('...g','called piiig')
Find('...g','called piiig much better:xyzg')
Find('x..g','called piiig much better:xyzg')
Find('..zg','called piiig much better:xyzg')
Find(r'c\.l','c.lled piiig much better:xyzgs')

Find(r':\w\w\w','blah:cat blah blah')
Find(r'\d\d\d','blah:123xxx')
Find(r'\d\s\d\s\d','1 2 3')
Find(r'\d\s+\d\s+\d','1   2           3')
Find(r':\w','blah blah:kitten blabh blah')
Find(r':\w+','blah blah:kitten blabh blah')
Find(r':\w+','blah blah:kitten123 blabh blah')
Find(r':\w+','blah blah:kitten123& blabh blah')
Find(r':.+','blah blah:kitten123& blabh blah')
Find(r':\S+','blah blah:kitten123123&a=123&yatta blabh blah')
Find(r'\w+@\w+','blah nick.p@gmail.com yatta')
Find(r'[\w.]+@\w+','blah:nick.p@gmail.com yatta')
Find(r'[\w.]+@[\w.]+','blah nick.p@gmail.com yatta')
Find(r'[\w.]+@[\w.]+','blah .nick.p@gmail.com yatta')
Find(r'\w[\w.]+@[\w.]+','blah .nick.p@gmail.com yatta')
Find(r'\w[\w.]*@[\w.]+','blah nick.p@gmail.com yatta')

m=re.search(r'([\w.]+)@([\w.]+)','blah nick.p@gmail.com yatta')
print(m.group())
print(m.group(1))
print(m.group(2))

n=re.findall(r'[\w.]+@[\w.]+','blah nick.p@gmail.com yatta foo@bar')
print(n)
b=re.findall(r'([\w.]+)@([\w.]+)','blah nick.p@gmail.com yatta foo@bar')
print(b)

print(dir(re))