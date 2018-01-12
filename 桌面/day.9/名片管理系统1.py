"""
名片管理系统v2.0
1. 添加一个新的名片
2. 删除一个名片
3. 修改一个名片
4. 查询一个名片
5. 显示所有名片
6. 退出系统
"""
# 1. 有一个容器来存储    这个时候我用list用来存储数据
card_infors = []

while True:
   # 2. 获取用户输入的内容
     num = int(input("请输入操作序号"))

   # 3. 根据用户输入的序号，进行相应的操作
     if num == 1: #添加一个名片
        # 1 ）用户来添加内容
         new_name = input("请输入新的名字")
         new_qq = input("请输入新的qq")
         new_wechat = input("请输入微信")
         new_addr = input("请输入地址")
         new_tel  = input("请输入电话")

        # 定义一个新的字典  用来存储新的名片

        # new_infor = {}
        # new_infor = ["name"] = new_name
        # new_infor = ["qq"] = new_qq
        # new_infor = ["wechat"] = new_wechat
        # new_infor = ["addr"] = new_addr
        # new_infor = ["tel"] = new_tel
        
         new_infor = {"name":new_name,"qq":new_qq,"wechat":new_wechat,"addr":new_addr,"tel":new_tel}
        # 把这个词典添加到列表里
         card_infors.append(new_infor)
        # 添加成功
        # print{"添加成功，现在的全部数据是%s"%card_infors}
         for name in card_infors:
             print("*"*50)
             for k,j in name.items():
                 print("名字%s:%s"%(k,j))
     elif num == 2: #删除一个名片
         name = input("请输入你想要删除的名片")
         index = 0
         for dic in card_infors:
             if dic["name"] ==name:
                 del card_infors[index]
             else:
                 index =+ 1
         for dic in card_infors:
             print("姓名\n%s\tqq\n%s\t"%(dic['name'],dic['qq'])
     elif num == 3:  #修改一个名片
         name = input("请输入你想要修改的名片")
         for dic in card_infors:
             if dic['name'] == name:
                 name2 = input("请输入您要替换的新名字")
                 dic['name'] = name2
     elif num == 4: #查询一个名片
         temp = input("请输入您要查询的名片")
         for name in card_infors:
             if temp in name_infors:
                 print("*"*50)
               if temp == name["name"]:
                     print("该用户存在")
                 else:
                     print("该用户不存在")        
     elif num == 5: #显示所有名片
         for s,h in card_infors:
             print("%s:%s"%(s,h))     
     else:
         break
         print("退出系统")
