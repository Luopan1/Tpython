# coding=utf-8
a = [(x, y) for x in range(0, 2) for y in range(0, 3)]
print(a)

b = ((x, y) for x in range(0, 2) for y in range(0, 3) if x % 2 == 0)
for temp in b:
    print(temp)

# 列表去重

c = [11, 22, 33, 44, 22, 33]
print(c)

d = {11, 22, 33, 44, 22, 44}  # 字典是不重复的
print(d)
