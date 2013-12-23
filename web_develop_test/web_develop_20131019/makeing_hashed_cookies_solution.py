__author__ = 'nancy'

import hashlib
import hmac
#Implement the hash_str function to use HMAC and our SECRET instead of md5

SECRET = "imsosecret"


def hash_val(s):
    return hmac.new(SECRET , s).hexdigest()


def hash_str(s):
    return hashlib.md5(s).hexdigest()

# print(hash_str("io"))
#implement the function make_secure_val,which tabkes a string and returns
#a string of the format:
#s,HASH

def make_secure_val(s):
    return "%s,%s" % (s, hash_str(s))

#implement the function check_secure_val,which takes a string of the format
#s,HASH
#and returns s if hash_str(s)==HASH,otherwise None

def check_secure_val(h):
    val = h.split(',')[0]
    if h == make_secure_val(val):
        return val


print(make_secure_val("cool"))
print(check_secure_val('cool,b1f4f9a523e36fd969f4573e25af4540'))