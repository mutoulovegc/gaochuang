def list(i):
    i[0] = i[0]+1
    return i
a = [2]
print(list(a))
print(a)
print ('-'*30)
def list2(i,item):
    i.append(item)
    return i
b = [4]
print(list2(b,5))
print(b)

def list3(c):
    c['age']=18
d = {'name':'高闯','age':18}
print(d)

