# coding=utf-8
# 需求：
#       使用property来升级私有化的get和set方法
class Test():
    def __init__(self):
        self.__num = None

    def setNum(self, newNum):
        self.__num = newNum

    def getNum(self):
        return self.__num

    num = property(getNum, setNum)  # 先写get方法  再写set方法  只能写方法名字  不能写成方法


t = Test()
t.num = 100
print(t.num)
print(t._Test__num)
