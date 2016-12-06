#!/usr/local/bin/python3
# -*- utf-8 -*- 
""" 实时读取正在运行的log日志

"""
import time
def follow(thefile):
    thefile.seek(0, 2)  # seek第一个参数表示当前行从第几个字符开始读取到最后一个字符，
    # 填0表示从第0个字符到该行最后一个字符，填10就表示从当前行第十个字符开始读取到当前行
    # 最后一个字符； 第二个参数有三种值，0表示从文件第一行开始读取，1表示接着上次的位置开始
    # 读取，2表示从最后一行开始读取
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1) # 让程序进入休眠状态0.1秒，避免io读写过于凶猛
            continue
        yield line

if __name__ == '__main__':
    try:
        logfile = open("/usr/local/tomcat7_rqt/logs/catalina.out")
        for line in follow(logfile):
            print(line)
    except FileNotFoundError as error:
        print('log file not found')


