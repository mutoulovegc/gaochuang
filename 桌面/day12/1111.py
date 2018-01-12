def register(account,passwd):
    f = open ('account.txt','w+')
    f.write(account)
    f.close()
    f2 = open('passwd.txt','w+')
    f2.write('passwd')
    f2.close()
def login(account,passwd):
    f = open('account.txt','r')
    b = f.readlines()
    
    f2 = open('passwd.txt','r')
    c = f2.readline()
    if account == c[0]:
        print('登录成功')
    f.close()
    f2.close()

#account = input('qing') 
#register()
#login()
