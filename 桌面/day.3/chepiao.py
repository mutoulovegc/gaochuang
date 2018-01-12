""
has_ticket = bool(input("请问是否有车票"))
if has_ticket == True:#表示有车票
    print("可以进入安检程序")
    knife_length = float(input("请输入刀的程度"))
    if knife_length >= 20:
        print("不可以允许上车")
    else:
        print("可以上车")
else:
    print("请去买票")
