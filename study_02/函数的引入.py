# coding=utf-8
"""def 函数名():"""


# 定义函数
def addName(a, b):
    print(a + b)


print("=" * 50)
addName(10, 20)

print("_" * 50)


# 带有返回值的函数

def get_temp():
    wend = 23
    return wend


def get_wendu():
   return get_temp() + 3
print("当前华氏温度是%d"%(get_wendu()))