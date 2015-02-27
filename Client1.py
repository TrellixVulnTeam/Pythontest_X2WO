#!/usr/bin/env python

######################
#   the client socket
######################

from socket import *

HOST = 'localhost'
PORT = 50000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpClientSock.send(data.encode())
    data = tcpClientSock.recv(BUFSIZE).decode()
    if not data:
        break
    print(data)

tcpClientSock.close()
