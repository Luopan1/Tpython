# coding=utf-8
# 需求：
#       使用property来升级私有化的get和set方法

# 注意 ******  set方法与get方法的名字是一样的 set方法前面是@方法名字.setter  get方法是直接@property  必须get方法写前面
class Test():
    def __init__(self):
        self.__num = None

    @property
    def number(self):
        return self.__num

    @number.setter
    def number(self, newNum):
        self.__num = newNum


t = Test()
t.number = 100
print(t.number)
print(t._Test__num)
