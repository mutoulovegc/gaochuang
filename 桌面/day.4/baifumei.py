#先判断是男是女如果是男 那就是高富帅，如果是女那就是白富美
sex = input("请问你是男的女的还是其他")
if sex == "男":
    height = input("你高吗")
    money = input("你富吗")
    handsome = input("你:wq帅吗")
    if height == "高" and money == "富" and handsome == "帅":
        print("高富帅")
    else:
        print("矮穷挫")
elif sex == "女":
    color = input("白")
    money = input("富")
    beautiful = input("美")
    if color == "白" and money == "富" and beautiful == ("美"):
        print("白富美")
else:
    die = input("是死还是活")
    if not die == "活":
        print("死人妖")
    else:
        print("活人妖")
