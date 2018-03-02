# coding=utf-8
def func(temp_func):
	def inner():
		return temp_func()
	
	return inner


@func
def test():
	return "hahah"


ret = test()
print("返回值是%s" % ret)
