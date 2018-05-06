#coding=utf-8
class Game:
        num=0

        def __init__(self):
            self.name="laowang"

        #类方法
        @classmethod
        def add_num(cls):
            cls.num=100

        @staticmethod
        def print_menu():
            print("-"*50)
            print("       穿越火线      ")
            print("      1.开始游戏      ")
            print("      2.结束游戏      ")
            print("-"*50)

game=Game();
game.add_num()
print(game.num)
print("-"*100)

Game.add_num()
print(Game.num)


print("**"*100)

Game.print_menu()
game.print_menu()