# coding=utf-8
"""匿名函数"""
# lambda 参数：式子

result = lambda x, y: x + y

print( result( 1, 2 ) )


# infors = [{"name:zhangsan", "age:18"}, {"name:lisi", "age:10"}, {"name:wangwu", "age:19"}]
# print( infors.sort( key=lambda x: x["age"] ) )

def test(a, b,fun):
    result = fun(a,b);
    print( result )

func=eval(input("请输入一个匿名函数"))#eval 将字符串转换成表达式的样子

test( 11, 22,func)
