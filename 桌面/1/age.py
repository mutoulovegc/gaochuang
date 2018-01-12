age = int(input('请输入年龄'))
if age < 2:
    print("婴儿")
elif age < 4:
    print("正在蹒跚学步")
elif age < 13:
    print("儿童，可以参加留六一儿童节")
elif age < 20:
    print("青年人")
else:
    print("成年人")
