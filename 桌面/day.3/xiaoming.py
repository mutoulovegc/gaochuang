"""
低于18.5 : "过轻"
18.5-25 : "正常"
25-28 : "过重"
28-32 : "肥胖"
高于35 : "严重肥胖"
"""
name = input("请输入你的名字")
weight = float(input("请输入你的重量"))
high = float(input("请输入你的身高"))
bmi = (weight / high)
if bmi < 18.5:
    print("姓名%s的bmi为%s结果过低"%(name,bmi))
elif bmi < 25:
    print("""""")
elif bmi < 28:
    print("""""")
elif bmi < 32:
    print("""""")
else:
    print("""""")
