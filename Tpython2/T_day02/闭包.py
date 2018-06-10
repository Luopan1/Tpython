# coding=utf-8
def Test(number):
    # 函数内部定义一个函数 并且这个函数用到了外边函数的变量 那么讲这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print("in test_in函数,number_in的值是%d" % number_in)
        return number + number_in

    return test_in


rect = Test(100)
print(rect(10))
