#coding=utf-8
class Cat:
    def __init__(self,new_name,new_age):
        self.name=new_name
        self.age=new_age

    def __str__(self):
        return "%s的年纪是%d"%(self.name,self.age)

    def eat(self):
        print("猫吃鱼")

    def introduce(self):

        print("%s的年纪是%d"%(self.name,self.age))

tom=Cat("汤姆",40)
print(tom)
print("="*50)
tom.introduce()