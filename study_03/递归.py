# coding=utf-8

def jiecheng(a):
    if (a > 1):
        return a * jiecheng(a - 1)
    else:
        return a


print(jiecheng(3))


def add(a):
    if a > 1:
        return a + add(a - 1)
    else:
        return a

print(add(5))


def Hanio():
    zhuZiOne=1
    zhuZiTwo=2
    zhuziThree=3
    disk1="disk1"
    disk1="disk2"
    disk3="disk3"