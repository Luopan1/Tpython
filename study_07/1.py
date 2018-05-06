# coding=utf-8
import sys

# name=sys.argv[1]
# print("传递的参数是%s"%name)
"""列表生成式"""
b = [i for i in range( 1, 18 )]
print( b )
b = [11 for i in range( 1, 18 )]
print( b )

c=[(x,y) for x in range(1,3) for y in range(11,22)]
print(c)

d=[i for i in range(10) if i%2==0]
print(d)