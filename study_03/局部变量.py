# coding=utf-8
wendu=0;
def get_wendu():
    #使用global 用来对全局变量申明 那么久不会再定义一个局部变量 从而对全局变量的更改
        global  wendu
        wendu=33

def print_wendu():
    print("温度是%d"%(wendu))

get_wendu()
print_wendu()