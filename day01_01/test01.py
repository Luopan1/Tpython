# encoding: utf-8


counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print (counter)
print (miles)
print (name)

x = "a"
y = "b"
print(x)
print(y)


# a,b,c,d=1,'2',2.2,1+2j
# print (type(a),type(b),type(c),type(d))

a = 11;
print (isinstance(a, int))


class A:
	pass


class B(A):
	pass


print (isinstance(A(), A))
print (type(A()) == A)

print (isinstance(B(), A))
print (type(B()) == A)

lists = [1, "add", 1 + 2j, 70.2]
print (lists)
