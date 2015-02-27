#!/usr/bin/env python

from socketserver import (TCPServer as TCP,
                    StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 22222
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline().decode())).encode())

tcpServer = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServer.serve_forever()





