# coding=utf-8
infor = {"name": "laowang", "age": 18}
print(len(infor))  # 打印的是键值对的个数
print(infor.keys())  # 打印出来的是一个列表  打印的字典的所有的键
print("=" * 50)
print(infor.values())  # 打印出来的是所有的值 也是一个列表

print("=" * 50)
if "name" in infor.keys():
    print(infor.get("name"))
print("*" * 50)
print(infor.items())
