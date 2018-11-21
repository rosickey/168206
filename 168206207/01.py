#!/usr/bin/python3
# -- coding: utf-8 -- 
'''¶ş·Ö²éÕÒ£¬µİ¹é'''
def binary_serach(list, item):
    low=0
    high=len(list)-1
    while low<=high:
        mid=int((low+high)/2)
        guess=list[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None
my_list=[1,3,5,7,9]

def bs3(list,item):
    mid=len(list)//2
    if list[mid]==item:
        return list[mid]
    if mid==0:
        return 0
    else:
        if item>list[mid]:
            return bs3(list[mid:],item)
        else:
            return bs3(list[:mid],item)
        
lis=[1,3,5,7,9,11,13,15]
print(bs3(lis,13)) 