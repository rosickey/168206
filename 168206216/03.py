#coding=utf-8
# 168206216 李金印
def fa(num):
    if num<3:
        return 1
    else:
        return fa(num-1)+fa(num-2)
for i in range(1,30):
    print(fa(i),end = ' ')