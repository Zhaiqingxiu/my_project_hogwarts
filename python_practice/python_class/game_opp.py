class Game:
    def __init__(self):
        self. my_hp = 1000
        self.my_power = 200
        self.enemy_hp = 1000
        self.enemy_power = 199

    def fight(self):
        while True:  # 一直执行，死循环，需要加break
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            # 判断谁的血量小于等于0
            if self.my_hp <= 0:
                print("我输了")
                # 满足条件，跳出循环
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break
    def rest(self,time_num):
        print(f"休息{time_num}分钟")

class HouYi(Game):
    #定义护甲属性
    def __init__(self,my_hp,enemy_hp):
        self.defense = 100
        #通过继承调用父类的构造函数，拿到父类的属性
        super().__init__()
    #改造fight方法
    def fight(self):
        while True:
            #修改my_hp计算方式
            self.my_hp = self.my_hp +self.defense- self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            if self.my_hp <= 0:
                print("我输了")
                # 满足条件，跳出循环
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break
game = HouYi(200,300)
game.fight()
game.rest(5)



