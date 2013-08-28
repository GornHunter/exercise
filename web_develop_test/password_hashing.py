__author__ = 'nancy'

import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in range(5))

print make_salt()

def make_new_hash(name,pw,salt=None):
    if not salt:
        salt=make_salt()
    h=hashlib.sha256(name+pw+salt).hexdigest()
    return '%s,%s'%(h,salt)

def valid_pw(name,pw,h):
    salt=h.split(',')[1]
    return h==make_new_hash(name,pw,salt)

h=make_new_hash('spez','hunter2')
print h
print valid_pw('spez','hunter2',h)
print make_new_hash('spez','hunter2')
