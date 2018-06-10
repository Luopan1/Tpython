a = [11, 22, 33]
b = [11, 22, 33]

if a == b:
    print("true")
else:
    print("false")
print(id(a))
print(id(b))

if a is b:
    print("true")
else:
    print("false")
    print("a的地址是%s" % id(a))
    print("b的地址是%s" % id(b))
# 等号 判断内容是否相等 是否是同一个
# is   判断引用是否同 即地址是否一样 在-6到126这个数字之间（不清晰）  is都是真的

c = a

if c is a:
    print("true")
    print("c的地址是%s" % id(c))
    print("a的地址是%s" % id(a))
else:
    print("false")
