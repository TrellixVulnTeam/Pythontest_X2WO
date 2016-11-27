#!/usr/bin/env python

from socket import *

HOST = '127.0.0.1'
PORT = 50003
BUFSIZE = 2048
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
