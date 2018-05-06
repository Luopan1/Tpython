#coding=utf-8
a="lao"
b="wang"
c="zhao"
d=a+b
print(d)

print("===%s==="%(a+b))
print(d[2])#取出d中的第二个字符 是从0开始的下标
try:
    print(d[9])
except:
    print("没有第10个字符")
print(d[len(d)-1])
print(d[-1])


"""字符串的切片"""

name="abcdefABCDEFG"
print(name[2:6])#包左不包右 取到cdef
print(name[2:])#不写第一个冒号之后的数字 默认取到最后一个

print(name[2:-1:2])#每取一个 跳一个再取 步长为正的时候 就是顺序的走

print(name[-1::-1])# 步长为负数的时候  就是逆序的走  并且 步长的大小影响了是否跳过某些指