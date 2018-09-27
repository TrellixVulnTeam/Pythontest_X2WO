__author__ = 'Zhanxueyou'
# coding:utf-8
import time
import urllib.request
import threading
from time import sleep

# 性能测试页面
PERF_TEST_URL = "http://test.www.999ask.com"

THREAD_NUM = 1000
ONE_WORKER_NUM = 10000
LOOP_SLEEP = 0.5

ERROR_NUM = 0

def doWork(index):
    t = threading.currentThread()
    try:
        html = urllib.request.urlopen(PERF_TEST_URL).read()
    except urllib.request.URLError as e:
        print("[" + t.name + " " + str(index) + "]")
        print(e)
        global ERROR_NUM
        ERROR_NUM += 1

def working():
    t = threading.currentThread()
    print("[" + t.name + "]Sub Thread Begin")
    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        doWork(i)
        sleep(LOOP_SLEEP)
    print("[" + t.name + "]Sub Thread End")


def main():
    t1 = time.time()
    Threads = []
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working, name="T"+str(i))
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

    for t in Threads:
        t.end()

    print("main thread end")

    t2 = time.time()
    print("++++++++++++++++++++++++++++++++")
    print("URL:", PERF_TEST_URL)
    print("任务数量：", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM*ONE_WORKER_NUM)
    print("总耗时（秒）：", t2-t1)
    print("每次请求耗时：", (t2-t1)/(THREAD_NUM*ONE_WORKER_NUM))
    print("每秒承载耗时：", 1/((t2-t1)/(THREAD_NUM*ONE_WORKER_NUM)))
    print("错误数量：", ERROR_NUM)

if __name__ == "__main__":
    main()
