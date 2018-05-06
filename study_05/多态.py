class Dog:
    def print_Self(self):
        print("你是狗 我们照顾你")
class XQQ(Dog):
    def print_Self(self):
        print("hello everyone  我是你的爸爸")

def introduce(temp):
    temp.print_Self()

dog1=Dog();
dog2=XQQ();
introduce(dog1)
