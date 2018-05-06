# coding=utf-8
import os

path = "/Users/ifind/Desktop/python/"
# path="111[备份].txt"
# os.rename(path,"111.txt")
# os.remove("111.txt")
# os.mkdir("hahah")
print( os.getcwd() )  # 获取当前路径

os.chdir( path )  # 改变路径
print( os.getcwd() )
#os.mkdir("haha") #创建文件夹
os.remove("2222")
f = open( os.getcwd() + "/2222.txt", "w" )  # 这个创建的是文件 不是文件夹

print( os.listdir() )
os.rmdir( "哈哈" )  # 删除文件夹  删除文件的是remove（"路径"）
