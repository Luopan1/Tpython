# coding=utf-8
import sys
class Cat:
    def __del__(self):
        print("猫不见了")


    def setCatIsVisable(self,isvisable):
        if isvisable:
            self.__del__()
        else:
            print("猫还在")


tom=Cat()
lanMao=tom
del lanMao

tom.setCatIsVisable(True)
print(sys.getrefcount(tom))