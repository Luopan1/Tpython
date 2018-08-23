from Tpython05.SQLHelper import *

try:
    dbHelper = DbHelper('104.224.166.169', "root", "135517", "python3", 3306, "utf8")
    SQL = "select * from students where name=%s"
    data = dbHelper.get_All(SQL, "郭靖")
    for d in data:
        # 注意int类型需要使用str函数转义
        print("ID: " + str(d[0]) + '  用户名： ' + str(d[1]) + "  年级： " + str(d[2]))

    insertSQL = "insert into students(name,age) values(%s,%s)"
    parames=["小六六",28]
    print(dbHelper.insert(insertSQL, parames))
except Exception as e:
    print(e)
