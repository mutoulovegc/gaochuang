print('欢迎来到阿里巴巴')
def add():
    ygrz_list = []
    name = input("请输入姓名")
    number = input("请输入工号")
    age = input("请输入年龄")
    job = input("请输入工作")
    money = input("请输入薪资")
    date = input("请输入入职日期")
    yuan_gong = {'姓名':name,'工号':number,'年龄':age,'工作岗位':job,'每月薪水':money,'入职日期':date}
    ygrz_list.append(yuan_gong)
    print(ygrz_list)




add()
