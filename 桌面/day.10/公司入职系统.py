"""
创建一个公司，
员工的报道
员工的入职
查询员工
开除员工
显示所有员工
"""
#公司入职系统

print('*'*40)
wood_yxgs = "欢迎进入木头科技有限公司"
print(wood_yxgs.center(40))

#有两个功能
#报道 入职

print("请您这边登记一下")
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

#登记成功，可以入职

name = input("请输入你的姓名")
idcard = input("请输入你的证件号")


#创建一个学历，职位的列表
#因为我的公司最低初中学历所以

print("你是gaochuang吗")

#while True:

 #    w = (input('请输入是否'))

#创建一个列表

education_list = [] 

#创建三个字典

a = {'education':'初中','job':'劳务部'}
b = {'education':'高中','job':'市场部'}
c = {'education':'大学','job':'人事部'}

education_list.append(a)
education_list.append(b)
education_list.append(c)

#报道
#定义自变量

#在链表里取出来一个字典
def entry():
    education = input("请输入你的学历")
    count = 0
    for dic in education_list: 
        if education == dic['education']:
            print(education_list[count]['job'])
        else:
            print("给我当助理吧")
            count += 1

