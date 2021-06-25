import random

def fight(enemy_hp,enemy_power):
    #定义四个变量用来储存数据
    my_hp = 1000
    my_power = 200
    #打印敌人的血量和攻击力
    print(f"敌人的血量为{enemy_hp},攻击力为{enemy_power}")
  #加入循环，让游戏可以多轮
    while True:#一直执行，死循环，需要加break
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        # print (my_hp)

        #判断谁的血量小于等于0
        if my_hp <= 0:
        #打印我和敌人的剩余血量
            print(f"我的剩余血量为{my_hp}，敌人的剩余血量为{enemy_hp}")
            print("我输了")
            #满足条件，跳出循环
            break
        elif enemy_hp <= 0:
            print(f"我的剩余血量为{my_hp}，敌人的剩余血量为{enemy_hp}")
            print("我赢了")
            break
if __name__ == "__main__":
    #利用列表推导式生成hp
    hp = [x for x in range(990,1010)]
    # print(hp)
    # print(type(hp))
    #让敌人的hp从hp列表中随机挑选一个值
    enemy_hp = random.choice(hp)
    print(enemy_hp)
    #敌人的攻击力randint方法生成随机整数
    enemy_power = random.randint(190,210)
    print(enemy_power)

    #调用函数，传入敌人的hp和power
fight(enemy_hp,enemy_power)


    #Alt+Enter自动导包
   #main入口函数的作用，条件成立，就会执行main下的东西
   #这个函数如果通过导包，调用得话，main下得东西别的文件不会执行
   #clone pull
   #第三次提交
