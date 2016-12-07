#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import time

p = subprocess.Popen('tail -f /usr/local/tomcat7_rqt/logs/catalina.out', 
shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
while True:
    line = p.stdout.readline()
    if line:
        print(line)     # 打印出来的是二进制字节码，需要解码
        print(line.decode())