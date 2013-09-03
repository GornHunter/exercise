__author__ = 'nancy'


import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('www.meituan.com', 80))

sock.send('GET / HTTP/1.1\r\nHost: www.meituan.com\r\n\r\n')
print sock.recv(8096)
# print sock.recv(8096)