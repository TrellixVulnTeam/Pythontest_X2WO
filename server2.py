#!/usr/local/bin python3
# -*- coding: utf-8 -*-
from socketserver import TCPServer, StreamRequestHandler
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('link from : ', addr)
        self.wfile.write('恭喜你链接成功'.encode())
server = TCPServer(('', 1234), Handler)
server.serve_forever()



