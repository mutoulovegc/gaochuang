
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
def sign(): 
	#从列表里取出来一个字典
    name = input("请输入你的姓名")
    idcard = input("请输入你的证件号")
#	for dic in name_list:

	#如果输入的名字等于公司记录的名字进行下一步

        #	if name == dic['name']:
	#验证身份证号
#		    if dic["idcard"] == idcard:
#			print("身份一致，可以入职")
#		    else:
#			print("证件号不对，不能入职")
#		else:
#		    print("身份不匹配，没有这个人")

   
#登记成功，可以入职

#创建一个学历，职位的列表

#因为我的公司最低初中学历所以

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
   
        count += 1

#中午了，去食堂吃饭

#食堂好多多好吃的

#创建一个列表



#'''
#1.创建一个菜谱：

#里面有菜单价格

#例如 菜名 黄瓜  价钱 1 

#2 添加菜

#3#.删除菜

#4.查询有什么菜

#5.退出


#创建个菜单，用这个添加菜名及价格


food_list = []

#i定义一个输出横线的函数

def pringtline():
    
    #输出函数横线
    
    print('*'*40)

#添加

def addFood():
    #菜名，价钱
    name = input("请问你吃什么")
    price = int(input("价钱什么"))
    #吧菜名保存到菜谱里
    #创建一个菜的价格
    cai_ming = {'菜名':name,'价钱':price} 
    #把这个菜名放进菜谱里
    food_list.append(cai_ming)
    #函数的调用
    print('现在有的菜%s'%cai_ming)
    #吧菜名添加到菜谱里
#删除
def delete():
 #想删除菜    
    name = input('不要什么')
    count = 0
    for dic in food_list:
        if dic['菜名'] == name:
            del food_list[count]
        else:
            count += 1
    print('此时有%s'%food_list)
#修改
def change():
    #要修改什么
    name = input("你要修改的菜名")
    count = 0
    for dic in food_list:
        if dic['菜名']==name:
            food_list[count]['菜名']=input("请输入名字")
            food_list[count]['价钱']=input("请输入价钱")
        else:
            count += 1
    print("此时有%s"%food_list)
#查询
def cha_xun():
    for dic in food_list:
        print('菜名%s\t价钱%s\t'%(dic['菜名'],dic['价钱']))
#退出
sign()
#调用函数
entry()
addFood()
addFood()
delete()
change()
cha_xun()
