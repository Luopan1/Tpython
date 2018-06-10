# coding=utf-8
class Person():
    def __init__(self):
        self.__num = None

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num


t = Person()
# t.setNum(2000)
print(t.getNum())
print(dir(t))
# print(t._Person__num)
