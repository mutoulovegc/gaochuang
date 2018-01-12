#需求是计算0-100偶数的累积球和
sum = 0
i = 0
while i <= 100:
    sum = sum + i
    i = i + 2
    print("he%d"%sum)
