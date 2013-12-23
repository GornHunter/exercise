__author__ = 'nancy'

import socket


s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect(('en.wikipedia.org', 80))

s.send('GET /wiki/Hypertext_Transfer_Protocol HTTP/1.1\r\n') # initial line
s.send('Host: en.wikipedia.org\r\n')
s.send('User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)\r\n')
s.send('\r\n')

while 1:
    buffer = s.recv(102400)
    if buffer:
        print buffer
    else:
        break


