# coding=utf-8
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func

    def run(self):
        for i in range(5):
            print(self.func)
            time.sleep(1)


def dance():
    return "dance"


def sing():
    return "singe"


myThread = MyThread(dance())
thread = MyThread(sing())
myThread.start()
thread.start()