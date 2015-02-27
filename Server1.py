#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 50000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpServerSock = socket(AF_INET, SOCK_STREAM)
tcpServerSock.bind(ADDR)
tcpServerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpClientSock, addr = tcpServerSock.accept()
    print('connected from:', addr)

    while True:
        data = tcpClientSock.recv(BUFSIZE).decode()
        if not data:
            break
        tcpClientSock.send(('[%s] %s' % (ctime(), data)).encode())
    tcpClientSock.close()

tcpServerSock.close()

    