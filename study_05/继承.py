# coding=utf-8
class Animal:
    def eat(self):
        print( "——————吃————————" )

    def drink(self):
        print( "——————喝————————" )

    def sleep(self):
        print( "——————睡————————" )

    def run(self):
        print( "——————跑————————" )


a=Animal();
a.eat()
a.drink()
a.sleep()
a.run()

print("-"*100)

class  Dog(Animal):
    def drink(self):
        print("狗喝牛奶")

wangcai=Dog();
wangcai.eat()
wangcai.drink()
wangcai.sleep()
wangcai.run()

def printStr():
    print("打印一句话")
