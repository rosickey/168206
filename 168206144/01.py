#-*- coding: utf-8 -*- 
def find(s,alist):
    if len(alist) == 1:
        if s == alist[0]:
            return 0
        else:
            return -1

    mid = int(len(alist)/2)

    if s == alist[mid]:
        return mid
    elif s>alist[mid]:
        return mid + find(s,alist[mid:])
    else:
        return find(s,alist[0:mid])

list = [0,1,2,4,5,7,8,9]
x=int(input("input:"))
num = find (x,list)
if num >= 0 :
    print ("下标为：",num)
else:
    print ("不存在！")
