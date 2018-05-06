# coding=utf-8
def func(temp_func):
	def inner(*args,**kwargs):
		return temp_func(*args,**kwargs)
	
	return inner


@func
def test():
	return "hahah"

"""无返回值"""
@func
def test2():
	print("-----2------")
@func
def test3(a,b):
	print("值是%s和%s"%(a,b))
	

ret = test()
print("返回值是%s" % ret)
test2()

test3(11,12)
