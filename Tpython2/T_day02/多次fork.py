# coding=utf-8
import os

ret = os.fork()
if ret == 0:
    print("----1-----")
else:
    print("----2-----")
ret = os.fork()
if ret == 0:
    print("----11-----")
else:
    print("----22-----")
    #
    #
    #               |
    #               /\
    #               1 2
    #              /\ /\
    #             11 22 11 22
    #
    #
    #
