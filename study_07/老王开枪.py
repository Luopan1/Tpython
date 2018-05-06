# coding =utf-8
class Person():
    def __init__(self, name):
        super( Person, self ).__init__()
        self.name = name
        self.gun = None
        self.hp = 100;

    def anzhuang_zidan(self, danJia_tem, zidan_temp):
        danJia_tem.baocun_zidan( zidan_temp )

    def anzhuang_danjia(self, gun_temp, danjia_temp):
        gun_temp.baocun_danjia( danjia_temp )

    def naQiang(self, gun_temp):
        self.gun = gun_temp

    def __str__(self):
        if self.gun:
            return "%s的血量为%d拿起了一把%s" % (self.name, self.hp, self.gun)
        else:
            return "%s的血量为%d他没有枪" % (self.name, self.hp)

    def koubanji(self, person_temp):
        self.gun.fire( person_temp )

    def diaoxue(self,shashangli):
        self.hp-=shashangli

class Gun():
    def __init__(self, name):
        super( Gun, self ).__init__()
        self.name = name
        self.danJiaList = None

    def baocun_danjia(self, danjia_temp):
        self.danJiaList = danjia_temp

    def __str__(self):
        if self.danJiaList:
            return "枪的名字是：%s，%s" % (self.name, self.danJiaList)
        else:
            return "枪中没有弹夹"

    def fire(self, diren):
        zidan_temp = self.danJiaList.tanchuzidan()
        if zidan_temp:
            zidan_temp.dazhong( diren )
        else:
            print( "弹夹中没有子弹了" )


class DanJia():
    def __init__(self, max_num):
        super( DanJia, self ).__init__()
        self.max_num = max_num
        self.zidan_list = []

    def baocun_zidan(self, zidan_temp):
        self.zidan_list.append( zidan_temp )

    def __str__(self):
        return "弹夹的信息为%d/%d" % (len( self.zidan_list ), self.max_num)

    def tanchuzidan(self):
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None


class ZiDan():
    def __init__(self, shashangli):
        super( ZiDan, self ).__init__()
        self.shashangli = shashangli

    def dazhong(self, diren_temp):
        diren_temp.diaoxue( self.shashangli )


def main():
    laowang = Person( "laoWang" )
    ak47 = Gun( "ak47" )
    danJia = DanJia( 20 )
    for i in range( 1, 16 ):
        ziDan = ZiDan( 10 )

        laowang.anzhuang_zidan( danJia, ziDan )

    laowang.anzhuang_danjia( ak47, danJia )
    laowang.naQiang( ak47 )
    print( laowang )

    gebi_laowang = Person( "隔壁老王" )
    laowang.koubanji(gebi_laowang)
    print(gebi_laowang)

if __name__ == '__main__':
    main()
