#!/usr/bin/env python



__author__ = 'nancy'

import cgi
import os


print "Content-type: text/html\r\n\r\n"

for key in os.environ.keys():
    print '<p>%s => %s</p>' % (key, os.environ[key])

print 'ok. this is a test'
