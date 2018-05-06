# coding=utf-8
def sum_3_add(a,b,c,type):

    if type==1:
        result = a + b + c
    elif type==2:
        result=(a+b+c)/3

    print("结果是：%d"%(result))

num1 = int(input("请输入第一个值："))
num2 = int(input("请输入第二个值："))
num3 = int(input("请输入第三个值："))

sum_3_add(num1,num2,num3,2)