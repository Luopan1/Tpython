# coding=utf-8

from Tpython05.SQLHelper import *


def main():
    dbHelper = DbHelper('104.224.166.169', "root", "135517", "python3", 3306, "utf8")

    name = input("请输入用户名:")
    password = input("请输入密码")

    sql = "select * from users where name=%s"
    parames = (name)
    result = dbHelper.get_one(sql, parames)
    if result == None:
        print("用户不存在")
    else:
        searchPass = "select password from users where name=%s"
        passResult = dbHelper.get_one(searchPass, name)
        print(passResult)
        if passResult[0] == password:
            print("登陆成功")
        else:
            print("密码错误")


if __name__ == '__main__':
    main()
