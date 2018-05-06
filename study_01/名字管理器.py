# coding = utf-8
print("=" * 50)
print("           名字管理系统")
print("=" * 50)
print("1：添加一个学生的名字")
print("2：删除一个学生的名字")
print("3：修改一个学生的名字")
print("4：查询一个学生的名字")
print("5：查看所有学生的名字")
print("6:退出系统")
print("=" * 50)
names = []
while True:
    num = int(input("请输入功能序号"))
    if num == 1:
        names.append(input("请输入学生的姓名"))
        print(names)
    elif num == 2:
        name = input("请输入要删除的学生的名字")
        if name in names:
            names.remove(name)
            print(names)
        else:
            print("输入的名字不存在")
        pass
    elif num == 3:
        print(names)
        index = int(input("请输入要修改的名字的下标"))
        if index > 0 and index <= len(names):
            newname = input("请输入你要更改的名字")
            names[index-1] = newname
            print(names)
        else:
            print("你输入的序号有误")

    elif num == 4:
        find_name = input("请输入你要查询的名字")
        if find_name in names:
            print("存在着个名字")
        else:
            print("不存在这个人")

    elif num == 5:
        print(names)
    elif num==6:
        break
    else:
        print("你出入的序号有误")
