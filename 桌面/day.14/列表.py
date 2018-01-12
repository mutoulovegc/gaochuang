l = [x for x in range(1,100) for y in range(2,x+1) if x%y != 0]
c = set(l)

print(c)
