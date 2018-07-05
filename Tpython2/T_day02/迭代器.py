# coding=utf-8
#   1.先生成一个生成器
b = (x for x in range(10))

# for temp in b:
#     print(temp)

from collections import Iterable

print(isinstance(b, Iterable))  # 判断是否可迭代的

# 迭代器

from collections import Iterator

a = [11, 22, 33]
# print(next(a)) 列表不是可迭代的

# a=(x for x in range(1,10))
b = iter(a)  # 将不可迭代的变成迭代的
print(next(b))
print(id(a))
print(id(b))
