def buySmoke(money):
    if money >= 12:
        return '烟'
    else:
        return "不够"
money = int(input('老师给钱'))
manyan = buySmoke(money)
print(manyan)
