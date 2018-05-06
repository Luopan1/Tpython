# coding=utf-8
def test1():
    pass


def test2():
    print("----test2()-----")


def test3():
    print("3------1")
    test2()
    print("3--------2")

test3()