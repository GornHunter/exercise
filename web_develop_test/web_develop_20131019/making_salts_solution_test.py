__author__ = 'nancy'

import hashlib
import random
import string

#implement the function make_salt() that returns a string of 5 random
#characters use python's random module

# print(string.letters)


def make_salt():
    return "".join(random.choice(string.letters) for x in range(5))

#implement the function make_pw_hash(name,pw) that returns a hashed password
#of the format:
#HASH(name+pw+salt),salt
#use sha256

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return "%s,%s" % (h, salt)

#implement the function valid_pw() that returns true if a user's password
#matchs its hash.You may need to modify make_pw_hash.

def valid_pw(name, pw, h):
    print(h)
    salt = h.split(",")[1]
    print(salt)
    return h == make_pw_hash(name, pw, salt)


h = make_pw_hash("spez", "hunter2")
print(h)
print(valid_pw("spez", "hunter2", h))

# print(make_salt())
# print(make_pw_hash('user', '123456'))
