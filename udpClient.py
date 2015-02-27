#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 22222
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpClient = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpClient.sendto(('%s'% data).encode(),ADDR)
    data = udpClient.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)

udpClient.close()
