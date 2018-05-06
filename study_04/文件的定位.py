#coding=utf-8
path="/Users/ifind/Desktop/python/111.txt"
f=open(path,"r")
print(f.read(1))

print(f.tell())

f.seek(0,1)

print(f.read(1))
f.seek(0,2)#光标摆到文件末尾 0：表示文件开头 1：表示当前位置 2：表示文件末尾
print(f.read(1))