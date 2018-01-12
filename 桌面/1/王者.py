wzry_list = [{'帐号':'gaochuang','密码':'123456'}]
#print(wzry_list)
account = []
mi_ma = []
name = input('请输入帐号')
passwd = input("请输入密码")
a = {'帐号':name,'密码':passwd}
wzry_list.append(a)
for dic in wzry_list:
    account.append(dic['帐号'])
    mi_ma.append(dic['密码'])
    if name in dic['帐号']:
        print('帐号已注册')
        break    
    else:
        print('帐号注册')
    b = {'帐号':'name','密码':'passwd'}
    wzry_list.append(b)
name = input('请输入帐号')
passwd = input('请输入密码')
c = name
d = passwd
account.append(c)
mi_ma.append(d)
if name in account:
    if passwd in mi_ma:    
        print("已登录")
    else:
        print('重新登陆')
