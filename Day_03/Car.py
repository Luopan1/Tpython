# coding=utf-8

class Car():
	def __init__(self, name, color, price):
		self.name = name
		self.color = color
		self.price = price
	
	def print_cat(self):
		print("%s的%s大概价钱在%s万左右" % (self.color, self.name, self.price))
	
	def move(self, direction):
		print("%s的%s的车向%s方向开了" % (self.color, self.name, direction))


class lanbijini(Car):
	def __init__(self, name, color, price):
		Car.__init__(self, name, color, price)


lanbo = lanbijini("兰博基尼", "橙色", "500")
lanbo.print_cat();
lanbo.move("东北")
