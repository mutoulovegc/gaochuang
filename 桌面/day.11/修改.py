def adda(a):
    print("修改前:",a)
    a+=1
    print("修改后:",a)
    return a
a = 3
print('函数内部操作厚的a:',adda(a))
print("函数外面的变量a:",a)
