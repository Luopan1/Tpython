# coding = utf-8
# info={键：值，键：值}
info = {"name": "banzhang", "addr": "shandong", "age": 18}
print("%s %s %d" % (info["name"], info["addr"], info["age"]))

"""字典的增删改查"""
info = {"name": "banzhang"}
info["age"] = 18  # 字典的添加 如果key不存在  则是添加 如果存在  则是修改
print(info)
del info["age"]  # 删除一个键值对
print(info)
print(info.get("name"))  # 查询某个键对应的值
