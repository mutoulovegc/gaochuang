class Restaurant:
   def p(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
    
   def describe_restaurant(self):
        print("欢迎光临")
        print("%s的烹饪方法是"%self.name,"%s"%self.type)
   def open_restaurant(self):
        print("餐馆正在营业")
#print(a.name,a.type)
class Admin(Restaurant):
    def a(self):
        self.flavors = []
gao = Admin()
gao.p("高闯","煮")
gao.describe_restaurant()
gao.open_restaurant()
print(Admin())
