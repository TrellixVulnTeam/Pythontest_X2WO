#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 50000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpClient = socket(AF_INET, SOCK_STREAM)
tcpClient.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpClient.send(data.encode())
    data = tcpClient.recv(BUFSIZE).decode()
    if not data:
        break
    print(data)

tcpClient.close()
    