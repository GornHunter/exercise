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