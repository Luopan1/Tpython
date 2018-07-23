# coding=utf-8
import threading
import time


def sayBye(i):
    print("拜拜%d"%i)
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=sayBye,args=(i,))
        t.start()
