# -*- coding: utf-8 -*-
# http 异步通信
import asyncore
import socket

class AsyncGet(asyncore.dispatcher):
    def __init__(self, host):
        asyncore.dispatcher.__init__(self)
        self.host = host
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 80))
        self.request = b'GET /index.html HTTP/1.0 \r\n\r\n'
        self.outf = None
        print('index.html from: ', host)
    def handle_connect(self):
        print('connect: ', self.host)
    def handle_read(self):
        if not self.outf:
            print('creating connect: ', self.host)
        self.outf = open('%s.txt' % self.host, 'ab')
        data = self.recv(8192)
        if data:
            self.outf.write(data)
    def writeable(self):
        return len(self.request) > 0
    def handle_write(self):
        num_sent = self.send(self.request)
    def handle_close(self):
        asyncore.dispatcher.close(self)
        print('Socket object closed at : ', self.host)
        if self.outf:
            self.outf.close()

if __name__ == '__main__':
    AsyncGet('www.rqbao.com')
    asyncore.loop()

