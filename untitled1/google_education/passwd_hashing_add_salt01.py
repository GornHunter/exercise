__author__ = 'nancy'

import random
import string

import hashlib

# implement the function make_salt() that returns a string of 5 random
# characters use python's random module

def make_salt():
    return ''.join(random.choice(string.letters) for x in range(5))

# print make_salt()

# implement the function make_new_hash(name,pw) that returns a hashed password
# of the format:
# HASH(name+pw+salt),salt
# use sha256

def make_pw_hash(name, pw,salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s|%s' % (h, salt)

# print make_pw_hash('spez','hunter2')

def valid_pw(name, pw, h):
    salt = h.split('|')[1]
    return h == make_pw_hash(name, pw, salt)


h = make_pw_hash('spez', 'hunter2')
print h
print valid_pw('spez', 'hunter2', h)