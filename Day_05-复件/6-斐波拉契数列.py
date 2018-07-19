# coding=utf-8

def creatNum():
	a, b = 0, 1
	for i in range(5):
		yield b
		# print(b)
		a, b = b, a + b


b=creatNum()
print(next(b))
