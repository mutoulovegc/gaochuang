#定义类
class Plant:
    def __int__(self):
        self.color = "绿色"
    def sun(self):
        print("放光")
    def shoot(self):
        print("发泡")
    def resist(self):
        print("当僵尸")

#jiangshi
class Zombit:
    def __int__(self):
        self.color = "灰色"
    def jump(self):
        print("跳")
    def eat(self):
        print("吃脑子")

#创建对象
xrk = Plant()
xrk.name = "向日葵"
xrk.color = "yellow"
xrk.blood = "五十"
print("内存地址1:",id(xrk))
print("%s颜色%s,%s"%(xrk.name,xrk.color,xrk.blood))
xrk.sun()
wd = Plant()
wd.name = "豌豆射手"
wd.color = "green"
wd.blood = "雪亮五十"
print("内存地址2:",id(wd))
print("%s颜色是%s,%s"%(wd.name,wd.color,wd.blood))
wd.shoot()
jg = Plant()
jg.name = "坚果"
jg.color = "grey"
jg.blood = "血量五百"
print("内存地址3:",id(jg))
print("%s颜色是%s,%s"%(jg.name,jg.color,jg.blood))
jg.resist()
ptjs = Zombit()
ptjs.name = "普通僵尸"
ptjs.speed = "50km/h"
ptjs.blood = "血量100"
print("内存地址4:",id(ptjs))
print("%s速度是%s,%s"%(ptjs.name,ptjs.speed,ptjs.blood))
ptjs.eat()
ttjs = Zombit()
ttjs.name = "跳跳僵尸"
ttjs.speed = "150km/h"
ttjs.blood = "血量200"
print("内存地址:",id(ttjs))
