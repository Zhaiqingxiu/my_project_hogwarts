def fight():
    #定义四个变量用来储存数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 199
  #加入循环，让游戏可以多轮
    while True:#一直执行，死循环，需要加break
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        print (my_hp)
        #判断谁的血量小于等于0
        if my_hp <= 0:
            print("我输了")
            #满足条件，跳出循环
            break
        elif enemy_hp <= 0:
            print("我赢了")
            break
fight()#调用定义的游戏函数
