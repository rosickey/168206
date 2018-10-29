#!/usr/bin/python3
# -- coding: utf-8 -- 
'''斐波那契数'''
'''def fb(num):
    if num<=2:
        return 1
    else:
        return fb(num-1)+fb(num-2)
for i in range(1,30):
    print(fb(i),end=" ")'''
def fa(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    list=[1,1]
    for i in range(2,n):
        list.append(list[-2]+list[-1])
    return list
if __name__=="__main__":
    x=int(input("请输入需要求个数："))
    print(fa(x))