import random
num = random.randint(1,100)
i = 0
while i <= 10 :
    player = (input("请输入你的数字"))
    if num == int(player):
        print("猜对了")
        break
    else:
        if num > int(player):
            print("猜小了")
        else:
           print("猜大了")
    i = i + 1
    
