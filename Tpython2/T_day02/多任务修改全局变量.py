# coding=utf-8
import os
import time

g_num = 100
ret = os.fork()
if ret == 0:
    print("线程1")
    g_num += 1
    print("线程1 g_num的值是：%d" % g_num)
else:
    time.sleep(3)
    print("线程2")
    print("线程2 g_num的值是：%d" % g_num)
