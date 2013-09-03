__author__ = 'nancy'

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('0.0.0.0', 9090))

sock.listen(1024)
while 1:
    print '--------------------------'
    client, addr = sock.accept()
    print client, addr

    buffer = client.recv(1024)
    client.send('this is from server')
    client.close()

    print buffer
