__author__ = 'nancy'

import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

print make_salt()

def make_new_hash(name,pw):
    salt=make_salt()
    h=hashlib.sha256(name+pw+salt).hexdigest()
    return '%s,%s'%(h,salt)
print make_new_hash('spez','hunter2')
