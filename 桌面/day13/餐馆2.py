class User:
    def __init__(self,first_name,last_name):
        self.first_name = "高闯"
        self.last_name = "郭丹"
    def describe_user(self):
        print(self.first_name,self.last_name)
    def greet_user(self):
        print("你好")
gao = User("高闯","木头")
gao.describe_user()
gao.greet_user()

