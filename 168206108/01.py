# -*- coding: utf-8 -*- 
def f(s,arr):
    if len(arr) == 1:
        return 0 if s == arr[0] else -100 # 4

    mid = int(len(arr)/2)

    if s == arr[mid]:
        return mid
    elif s > arr[mid]:
        return mid + f(s,arr[mid:])
    else:
        return f(s,arr[0:mid])
#测试----------------------------------
list = range(1,12,2)#包含从1到12（不包括12）的有序列表,间隔2
for x in range(0,12):
    num = f(x,list)
    if num >= 0 :
        print f(x,list)
    else:
        print "False！"
