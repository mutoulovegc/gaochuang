#公司入职系统
print('*'*40)
wood_yxgs = "欢迎进入木头科技有限公司"
print(wodd_yxgs.center(40))
#有两个功能
#报道 入职
print("*"*40)
print("功能1：%s\n功能2：%s\n"%("报道","入职"))
print("*"*40)
#创建个列表查看他是否被录取
name_list = [{'name':'gaochuang','idcard':'2107821995'}]
#报道
#创建一个函数
def sign(name='gaochuang',idcard='2107821995'):
#从列表里取出来一个字典
    for dic in name_list:
#如果输入的名字等于公司记录的名字进行下一步
        if name == dic['name']:
#验证身份证号
            if dic["idcard"] == idcard:
                print("身份一致，可以入职")
            else:
                print("证件号不对，不能入职")
        else:
            print("身份不匹配，没有这个人")
name = input("请输入你的帐号")
idcard = input("请输入你的密码")
sign(name,idcard)
