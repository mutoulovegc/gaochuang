print("欢迎来到阿里")
age = int(input("请输入你的年龄"))
xueli = int(input("请输入你的学历"))
#初中 = 1 ,高中 = 2 ,大学 = 3:
if age>18 and xueli>1:
    print("入职")
elif age>18 or xueli>1:
    print("下一论")
else:
    print("出门左转")
