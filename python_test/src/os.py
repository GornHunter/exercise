__author__ = 'Nancy'

import sys
import os
# print(dir(os))
#
# print(help(os))

def List(dir):
    filenames=os.listdir(dir)
    print(filenames)

def main():
    List(sys.argv[1])