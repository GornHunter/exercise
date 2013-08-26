__author__ = 'nancy'

import hashlib


def hash_str(s):
    return hashlib.md5(s).hexdigest()


def make_secure_val(s):
    return "%s,%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split(',')[0]
    if h == make_secure_val(val):
        return val


print make_secure_val("udacity!")
print check_secure_val("udacity!,e0e363931c518dc502391b2ab5cf6af2")



