# coding=utf-8
coolLeveal = 0


class CookDiGua:
    def __init__(self):
        self.cookString = "生的"
        self.Condments = []

    def __str__(self):
        s = "地瓜的状态是：%s，添加的佐料有%s" % (self.cookString, str(self.Condments))
        return s

    def cook(self, cookTime):
        global coolLeveal
        coolLeveal += cookTime
        if coolLeveal >= 0 and coolLeveal < 3:
            self.cookString = "生的"
        elif coolLeveal >= 3 and coolLeveal < 5:
            self.cookString = "半生不熟的"
        elif coolLeveal >= 5 and coolLeveal < 8:
            self.cookString = "熟了"
        elif coolLeveal >= 8:
            self.cookString = "燃起来了"

    def addCondments(self, condments):
        self.Condments.append(condments)


cookDiGua = CookDiGua()
cookDiGua.cook(3)
cookDiGua.addCondments("番茄酱")
print(cookDiGua)
cookDiGua.cook(5)
cookDiGua.addCondments("盐")
print(cookDiGua)
