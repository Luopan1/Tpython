# coding=utf-8
a1 = "laowang"
b1 = "zhaosi"
c1 = "wangwu"
names = ["laowang", "zhaosi", 1234]
"""列表的增加"""
names.append(12121)  # 列表的增加使用append()方法 追加到后面
names.insert(1, "悟空")  # 列表中的插入使用insert()方法 前面放插入的位置 从0开始的
names2 = ["葫芦娃", "爷爷", "蛇精"]
names.extend(names2)  # 将另外一个列表合到旧列表中 也可以使用names+=names2
print(names)

"""列表的删除"""
names.pop()  # 默认删除最后一个
print(names)
names.remove("葫芦娃")  # 根据内容删除
print(names)

print(names[-1::-1])
del names[0]  # 根据下标来删除
print(names)
"""列表的元素的更改"""
names2[0] = "沙师弟"
print(names2)

"""列表的查询"""
print("============================")
print(names)
names.remove("zhaosi")
if "zhaosi" not in names:
    print("不在  可以添加")

