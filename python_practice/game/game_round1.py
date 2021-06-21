
#根据缩进判断代码块的从属
#定义fight函数实现游戏逻辑

# def fight():
#     #定义四个变量用来储存数据
#     my_hp = 1000
#     my_power = 200
#     enemy_hp = 1000
#     enemy_power = 200
#     my_final_hp =my_hp - enemy_power
#     enemy_final_hp = enemy_hp -my_power
#     if my_final_hp > enemy_final_hp:
#         print("我赢了")
#     elif my_final_hp <enemy_final_hp:
#         print("我输了")
#     else:
#         print("平局")

#注释快捷键 ctrl+/

def fight():
    #定义四个变量用来储存数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200
    my_final_hp =my_hp - enemy_power
    enemy_final_hp = enemy_hp -my_power
    print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")


#复制当前行代码 :ctrl+d
