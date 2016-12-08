from time import ctime, sleep
import threading
def music():
    for i in range(4):
        print('I am listening music. %s' % ctime())
        sleep(2)

def movie():
    for i in range(4):
        print('I am watching movie. %s' % ctime())
        sleep(3)

threads = []
t1 = threading.Thread(target=music)
t2 = threading.Thread(target=movie)
threads.append(t1)
threads.append(t2)
for t in threads:
    t.setDaemon(True)
    t.start()
