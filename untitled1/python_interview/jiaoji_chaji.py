# -*- coding:utf-8 -*-
__author__ = 'nancy'

#/bin/env python


import sys
import codecs

print sys.version_info.major

# sys.setdefaultencoding('utf-8')

def reprunicode(u):
    if isinstance(u, list):
        return map(reprunicode, u)
        # for i in u:
        #     print i.decode('utf8')
    return repr(u).decode('raw_unicode_escape')


# intersection and deference set

a1 = [1, 2, 3, 4, 5]
a2 = [3, 2, 5, 7, 9]

# print [val for val in a1 if val in a2]
# print [val for val in a1 if val not in a2]

f = codecs.open("/home/nancy/interview_test/11", encoding='utf-8')
a = f.readlines()
f.close()

f = codecs.open("/home/nancy/interview_test/22", encoding='utf-8')
b = f.readlines()
t = [('亀',), ('犬',)]
print reprunicode(b)
diff = [val for val in b if val not in a]
f.close()

f = open("/home/nancy/interview_test/diff", 'w')
# f.writelines(diff)
f.close()

print reprunicode(a)
print reprunicode(b)
print reprunicode(diff)




