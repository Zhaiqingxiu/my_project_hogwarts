# class 类名：#驼峰命名
#     类属性 。。。
#     类方法 。。。
class House:
    #静态属性 ->类变量 (类之中，方法之外)
    door = "red"
    floor = "white"

    #构造函数，在类实例化的时候执行，构造函数就一个
    def __init__(self):#
        # 在方法中调用类变量，加self
        print(self.door)
        #实例变量，类当中，方法当中，以self.变量名的方式定义
        self.kitchen = "cook"

    #动态方法
    def sleep(self):
        #普通变量，在类当中，方法当中，前边没有self
        bed = "席梦思"
        self.table = "桌子可以放东西"
        print(f"在房子里可以躺在{bed}睡觉")

    def cook(self):
        print(self.kitchen)
        print("在房子里可以做饭吃")

# #把类实例化
# #北欧风房子
north_house = House()

# 中式风房子
china_house = House()
#调用类属性
print(House.door)
#修改类属性
House.door = "white"
print(House.door)
#用实例对象调用类属性

print(north_house.door)
#修改对象属性
north_house.door = "black"
print(north_house.door)
print(House.door)

north_house.sleep()
north_house.cook()
print(north_house.table)