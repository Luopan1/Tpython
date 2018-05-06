# coding=utf-8
class Cat:
    """初始化对象"""

    def __init__(self, new_name, new_age, new_color):
        self.name = new_name
        self.age = new_age
        self.color = new_color

    def eat(self):
        print( "猫吃鱼" )

    def drink(self):
        print( "猫喝可乐" )

    def introduce(self):
        print( "姓名是：%s     年龄是：%d   颜色是：%s" % (self.name, self.age, self.color) )


# 创建一个对象
tom = Cat( "汤姆", 40, "橘色" )
"""添加属性"""
tom.name = "汤姆猫"
tom.food="鱼"

# tom.age = "40"
# tom.color="橘色"
tom.introduce()

tom.eat()
"""第一种方式调用属性"""
print("姓名是：%s     年龄是：%d   零食是：%s"%(tom.name,tom.age,tom.food))
"""第二种"""

# tom_cat = Cat()
# tom_cat.name = "蓝猫"
# tom_cat.age = "10"
# tom_cat.color = "蓝色"
#
# tom_cat.introduce()
