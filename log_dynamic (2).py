#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import time

p = subprocess.Popen('tail -f /usr/local/tomcat7_rqt/logs/rqt.log', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
while True:
    line = p.stdout.readline()
    if line:
        print(line.decode('utf-8', 'ignore'))
