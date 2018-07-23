# coding=utf-8
def time_func(arg):
	def func(funcName):
		def inner():
			print("-----记录日志-----%s"%arg)
			funcName()
		return inner
	return func

@time_func("hehehe")
def test():
	print("----test----")


test();
