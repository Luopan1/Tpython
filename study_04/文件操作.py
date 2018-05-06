# coding=utf-8
"""在pyhon中使用open打开一个已经存在的文件  或者新建一个文件    open(文件名，访问模式)"""
f=open("/Users/ifind/Desktop/python/111.txt","w")
f.write("#hello World")
f.close()