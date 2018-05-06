#coding=utf-8
# import  study_05.继承
from study_05.继承 import printStr
class CarStore:
    def order(self,money):
        if money>50000:
            return Car()


class Car:
    def move(self):
        print("车在动")

cart_store=CarStore()
car=cart_store.order(100000)
car.move()

printStr()



