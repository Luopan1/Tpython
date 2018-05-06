# coding=utf-8
import random

one = int(input("请输入剪刀（0）石头（1）布（2）"))

two = random.randint(0, 2)

if (one == 0 and two == 2) or (one == 1 and two == 0) or (one == 2 and two == 1):
    print("你赢了")
elif one == two:
    print("平局 再来")
else:
    print("你输了")

print("电脑出了%d" % two)
