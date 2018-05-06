# coding=utf-8
path="/Users/ifind/Desktop/python/111.txt"
f = open(path, "r")
content = f.read()
f.close()

point=path.rfind(".")
destPath=path[0:point]+"[备份]"+path[point:]

copy = open(destPath, "w")
copy.write(content)
copy.close()
