# 两两不需要时间时
# 烧烤所需的时间
def bak(c, t):
    a = int((c-1) / 8)
    t = t + (a+1)*180 + 10
    return t


# 总花费时间
def time(c):
    t = 0
    t = bak(c, t)
    return t


# 顾客在吧台平均等待时间（只有顾客数超20才需要等待）
def wb(c):
    if c < 21:
        t = 0
    else:
        a = int((c - 1) / 20)
        t = (a * 10)/c
    return t


# 顾客在烧烤架等待时间
def ws(c):
    if c < 9:
        t = 0
    else:
        a = int((c - 1) / 8)
        b = int((c - 1) / 20)
        t = (a * 180 - b * 10) / c
    return t


print(time(1))
print(time(8))
print(time(25))
print(time(100))
print(ws(9))


# 两两相距60S时
# 当全部顾客进入吧台挑完材料的所需时间
def cus(c):
    t = (c - 1) * 60 + 10
    return t


# 总花费时间
def time(c):
    t = cus(c)+180
    return t
#当两两相距60S时，吧台不需要等待，烧烤架最多会烤三份食物，也不需要等待
print(time(25))


# 两两相距120S时
# 当全部顾客进入吧台挑完材料的所需时间
def cus(c):
    t = (c - 1) * 120 + 10
    return t


def time(c):
    t = cus(c)+180
    return t
#当两两相距60S时，吧台不需要等待，烧烤架最多会烤1.5份食物，也不需要等待
print(time(100))
