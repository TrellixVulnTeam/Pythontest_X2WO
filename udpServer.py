#!/usr/bin/env python
from socket import *
from time import ctime

HOST = ''
PORT = 22222
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpServer.recvfrom(BUFSIZ)
    udpServer.sendto(('[%s] %s' % (ctime(), data)).encode(), addr)
    print('...received from and returned to:', addr)

udpServer.close()
