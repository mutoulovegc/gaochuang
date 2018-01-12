row = 1
while row <=9:
    line = 1
    while line <= row:
        print("%d*%d=%d"%(row,line,row*line),end='\t')
        line += 1
    print("")
    row += 1
