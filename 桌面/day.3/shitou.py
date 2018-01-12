#假设电脑只会出石头    石头代表：1
computer = 1
#人要出什么  输入
player = int(input("请输入你的拳头"))

#开始我们的判断内容   电脑是石头
"""
如果人出2代表剪刀 人输了电脑赢了
如果人出3代表布 人赢了电脑输了
如果人出1代表石头 平手
"""
if player == 2:
    print("电脑赢了")
elif player == 3:
    print("人赢了")
else:
    print("平局")
