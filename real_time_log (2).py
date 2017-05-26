#!/usr/local/bin/python3
# -*- utf-8 -*- 
""" 实时读取正在运行的log日志

"""
import time
def follow(thefile):
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    try:
        logfile = open("/usr/local/tomcat7_rqt/logs/catalina.out")
        for line in follow(logfile):
            print(line)
    except FileNotFoundError as error:
        print('log file not found')


