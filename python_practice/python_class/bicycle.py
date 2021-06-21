'''
掌握类属性的方法和调用

'''
#自行车类
class Bicycle:
    def run(self,km):
        print(f"一共用脚骑了{km}公里，累死了")

#电动自行车类
#继承：把父类的名称放在类名后边的小括号
class EBicycle(Bicycle):
    #属性需要传参定义，可以直接放在构造函数中
    def __init__(self,valume):
        self.valume = valume
    #充电方法
    def fill_charge(self,vol):
        #充电后的电量 = 本身的电量 + 充电电量
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量为{self.valume}")
    def run(self,km):
       #1.获取目前电量所能电动骑行的里程数
        power_km = self.valume *10
        if power_km >= km:
            print(f"使用电瓶电量骑行了{km}公里")
        else:
            # 电量不够了，电骑行完了后，还得用脚骑行
            print(f"使用电瓶电量骑行了{power_km}公里")
            # 当电量消耗尽时，用bicycle的run骑行
            # # 非继承调用
            # bike = Bicycle()
            # bike.run(km-power_km)
            # 继承调用
            super().run(km-power_km)
ebike = EBicycle(10)
ebike.fill_charge(2)
ebike.run(150)
