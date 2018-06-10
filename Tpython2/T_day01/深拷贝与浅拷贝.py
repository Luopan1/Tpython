# coding= utf-8

a = [11, 22, 33]

b = a  # 浅拷贝

print(id(a))
print(id(b))

import copy

c=copy.deepcopy(a)
print(id(c))