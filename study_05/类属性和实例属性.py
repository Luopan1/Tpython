#coding=utf-8
class Tool:
    #属性
    num=0;

    def __init__(self,new_name):
        self.name=new_name
        Tool.num+=1

tool1=Tool("铁锹")
tool1=Tool("工兵铲")
tool1=Tool("水桶")
print(Tool.num)
