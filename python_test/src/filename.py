__author__ = 'Nancy'

import sys

# 1. program, 2-----n params
print(sys.argv)


for idx, arg in enumerate(sys.argv):
    print(idx, arg)


if len(sys.argv) < 2:
    print("Usage: \nfilename.py filename")
else:
    filename = sys.argv[1]
    try:
        f= open(filename, 'rU')
        for line in f:
            pass
            #print(line, end="")
    except Exception as e:
        # print(e)
        pass
#        raise e
