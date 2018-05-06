# coding=utf-8

str="hello world  python java android swift"
print("___________字符串对其方式__________")
print(str.rjust(50))
print("_"*50)
print(str.ljust(50))
print("_"*50)
print(str.center(50))

print("___________字符串去除两边的空格__________")

test="       1234124312421   1  "
print(test)
print(test.lstrip())
print("_"*50)
print(test.rstrip())
print("_"*50)
print(test.strip())

print("___________字符串的分割__________")

print(str.partition("python"))#按照python字符串将元字符串分割成三部分 打印成元祖
print(str.rpartition(" ")) #按照右边的第一个空格 分割成三部分

file_content="123\n1234124\n321234214\n123412\naa"
print(file_content.splitlines())

print("___________字符串的判断__________")

a="1341243"

print(a.isalpha())#是否是纯字母
print(a.isdigit())#是否是纯数字
print(a.isalnum())#是数字或者字母或者字母与数字的组合 返回true
print(a.isspace())#判断是否是纯空格
names=["aa","bb","cc"]
print(a.join(names))#将列表中的数据按照a一一组合 生成新的字符串
