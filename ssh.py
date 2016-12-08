#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import paramiko
import time

def ssh2(ip, username, password, cmd):
    """     连接ssh输出静态内容
    
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, username, password, timeout=5)
    for m in cmd:
        stdin, stdout, stderr = ssh.exec_command(m)
        for o in stdout.readlines():
            print(o)
    ssh.close()

def ssh2_dynamic(ip, username, password, cmd):
    """     连接ssh输出实时日志
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,22,username, password,timeout=5)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while True:
        print(stdout.readline())
        time.sleep(0.1)
    ssh.close()

ssh2('123.57.77.184', 'root', 'f!e!DV44haLAZNbN', ['ls -l'])
