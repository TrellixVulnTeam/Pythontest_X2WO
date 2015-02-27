#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 22222
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpClientSock = socket(AF_INET, SOCK_STREAM)
    tcpClientSock.connect(ADDR)
    data = input('>')
    if not data:
        break
    tcpClientSock.send(('%s' % data).encode())
    data = tcpClientSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)

tcpClientSock.close()