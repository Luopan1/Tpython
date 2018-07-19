# coding=utf-8
import types


class Person():
	def __init__(self, temp_name, temp_age):
		self.name = temp_name
		self.age = temp_age
	
	def println(self):
		print("%s的年龄是%s" % (self.name, self.age))


def run(self):
	print("%s正在跑" % self.name)


@staticmethod
def eat():
	print("吃饭了")


@classmethod
def sleep(cls):
	print("睡觉")


laowang = Person("老王", "30")
laowang.println()

laowang.run = run
laowang.run(laowang)

laowang.run = types.MethodType(run, laowang)
laowang.run()
Person.eat = eat
laowang.eat()

Person.sleep = sleep
laowang.sleep()


class Student():
	"""限定类的属性  不能添加别的属性 添加sex属性的时候就会崩溃"""
	__slots__ = ("name", "age")

s1 = Student()
s1.name = "学生1"
s1.age = "15"
s1.sex = "男"
