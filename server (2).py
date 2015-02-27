#!/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 50000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpServer = socket(AF_INET, SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(15)

while True:
    print('waiting for connection...')
    tcpClient, addr = tcpServer.accept()
    print('...connected from:', addr)

    while True:
        data = tcpClient.recv(BUFSIZE).decode()
        if not data:
            break
        tcpClient.send(('[%s] %s'%(ctime(), data)).encode())

    tcpClient.close()

tcpServer.close()

