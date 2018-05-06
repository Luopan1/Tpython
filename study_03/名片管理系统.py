# coding=utf-8

g_card_info = []


def print_menu():
    print("_" * 50)
    print("1.添加一个名片")
    print("2.修改一个名片")
    print("3.删除一个名片")
    print("4.查询一个名片")
    print("5.退出系统")


def add_new_card_info():
    """ 添加新的名片 """
    global g_card_info
    g_new_card = {}
    new_name = input("请输入添加的姓名")
    new_contact = input("请输入添加的联系方式")
    new_address = input("请输入添加的地址")
    g_new_card["name"] = new_name
    g_new_card["contact"] = new_contact
    g_new_card["address"] = new_address
    g_card_info.append(g_new_card)
    print(g_card_info)


def change_card_info():
    global  g_card_info
    print(g_card_info)
    _name = input("请输入你要更改学生的姓名")
    # 遍历列表 然后获取到字典 根据字典的key 去获取到名字  然后更改名字
    for temp in g_card_info:
        # print(temp)  测试
        if _name == temp["name"]:
            change_name = input("请输入你要更改的姓名")
            temp["name"] = change_name
            print(g_card_info)
            break
    else:
        print("你要修改的学生不存在")


def delete_card():
    global  g_card_info
    print(g_card_info)
    index = int(input("请输入你要删除的下标"))
    if index >= 0 and index <= len(g_card_info):
        del g_card_info[index - 1]
    else:
        print("下标超出范围")


def query_card_info():
    global  g_card_info
    quey_name = input("请输入你要查询的名字")
    for temp in g_card_info:
        if quey_name == temp.get("name"):
            print(temp)


while True:
    print_menu()
    try:
        type = int(input("请输入功能序号"))
    except:
        print("你输入的序号不对")
    if type == 1:
        add_new_card_info()
    if type == 2:
        change_card_info()
    if type == 3:
        delete_card()
    if type == 4:
        query_card_info()
    if type == 5:
        break
