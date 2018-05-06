#coding=utf-8
class SweetPotato:
    def __init__(self):
        self.cookedString="生的"
        self.cookedLevel=0
        self.condiments=[]

    def cook(self,cook_time):

        self.cookedLevel+=cook_time

        if self.cookedLevel>0 and self.cookedLevel<=3:
            self.cookedString="生的"

        elif self.cookedLevel>3 and self.cookedLevel<=5:

            self.cookedString="半生不熟"
        elif self.cookedLevel>5 and self.cookedLevel<=8:

            self.cookedString="熟了"
        elif self.cookedLevel>8:

            self.cookedString="糊了"


    def addCondiments(self,condiments):
        self.condiments.append(condiments)

    def __str__(self):
        return  "地瓜的状态是：%s(%d) s佐料是：%s"%(self.cookedString ,self.cookedLevel,str(self.condiments))

if __name__=="__main__":
    di_gua=SweetPotato();
    di_gua.cook(1)
    print(di_gua)
    di_gua.addCondiments("番茄酱")
    di_gua.cook(1)
    print(di_gua)
    di_gua.cook(1)
    print(di_gua)
    di_gua.cook(1)
    di_gua.addCondiments("大蒜")
    print(di_gua)
    di_gua.cook(1)
    print(di_gua)

