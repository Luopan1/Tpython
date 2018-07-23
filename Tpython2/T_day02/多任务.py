# coding=utf-8
import os
import time

ret = os.fork()  # 有两个返回值 第一次返回主线程的 第二次返回子线程的  子线程永远返回0
print("ret的值是：%d  线程是：%d" % (ret, os.getpid()))
if ret == 0:  # 子线程
    print("子线程是：%d" % os.getpid())
    print("主线程是：%d" % os.getppid())
    time.sleep(5)
    print("hahaha")
else:  # 主线程
    print("线程是：%d" % os.getpid())
    time.sleep(3)
    print("哈哈哈哈哈")

print("---over---")
