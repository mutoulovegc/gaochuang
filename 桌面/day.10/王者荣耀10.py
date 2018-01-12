wzry = "王者荣耀系统"
print(wzry.center(50))
print("*"*50)
print("功能一:%s/n,功能二:%s/n"%("登录","注册"))
print("*"*50)
account_list = [{'name':'gaochuang','passwd':'123456'}]
def login(account='gaochuang',passwd='123456'):
    print("登录")
    for dic in account_list:
        if account == dic['name']:
            if dic['passwd'] == passwd: 
                print("登录成功")
            else:
                print("密码错误")    
        else:
            print("帐号输入错误")
def register(zhanghao="高闯",mima="123456"):
    #print("注册")
    for dic in account_list:
        if dic['name'] ==zhanghao:
            print("您的账号被注册")
        else:
            tempDic = {}
            tempDic['name']=zhanghao
            tempDic['passwd']=mima
            account_list.append(tempDic)
            print("帐号创建成功")
            break
          

account = input("请输入帐号")
passwd = input("请输入密码")
#login(account,passwd)
register(account,passwd)
print(account_list)






