# coding=utf-8

# python2和python3的输入是不一样的  python2中使用的是raw_python(因为Python2中使用input会将输入的当代码执行)
high = input("请输入你的身高\n")
high_num = int(high)

"""if high_num >= 18:
    print("你可以去网吧了")
else:
    print("你还不可以去网吧")"""

name="laowang"
age=29
address="四川"

print("姓名是：%s_______年龄是：%d______地址是：%s"%(name,age,address))