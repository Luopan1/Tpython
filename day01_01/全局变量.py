# coding=utf-8

money = 1;


def addMoney():
	global money
	money = money + 1
	return money


print(money)
print(addMoney())
print(money)
