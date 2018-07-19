# coding=utf-8
def w1(func):
	print("装饰——1")
	def inner():
		print("验证权限w1")
		func()
	return inner


def w2(func):
	print("装饰——2")
		#将inner()返回 带到w1()里面去
	def inner():
		print("验证权限w2")
		func()
	return inner

"""装饰器 遇到函数 才执行 所以先走w2  然后将w2的inner()函数作为返回值  带给w1 然后再走w1的inner函数 """
@w1
@w2
def f1():
	print("__________f1___________")


f1()
