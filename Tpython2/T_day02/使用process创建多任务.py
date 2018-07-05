# coding=utf-8
from multiprocessing import Process
import os
import time


def run_proc(name):
    time.sleep(5)
    print("子线程运行中，name=%s,pid=%d..." % (name, os.getpid()))


if __name__ == '__main__':
    print("父进程 %d" % os.getpid())
    p = Process(target=run_proc, args=("test",))
    p.start()
    p.join()
    p.terminate()
    print("执行结束")
