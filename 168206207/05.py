#!/usr/bin/python3
# -- coding: utf-8 -- 
'''πÈ≤¢≈≈–Ú'''
def guibing(list1,list2):
    list3=[]
    i=j=0
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list2[j])
            j+=1
    if i==len(list1):
        for a in list2[j:]:
            list3.append(a)
    else:
        for a in list1[i:]:
            list3.append(a)
    return list3        
def merge_sort(lists):
    if len(lists)<=1:
        return lists
    mid=len(lists)//2
    left=merge_sort(lists[:mid])
    right=merge_sort(lists[mid:])
    return guibing(left, right)


if __name__=="__main__":
    alist=[5,7,3,0,2,4,90,8,80,999,9]
    print(merge_sort(alist))