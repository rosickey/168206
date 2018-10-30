# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#QuickSort by Alvin

def QuickSort(myList,start,end):
    if start < end:
        i,j = start,end
        base = myList[i]
        while i < j:
            while (i < j) and (myList[j] >= base):
                j = j - 1
            myList[i] = myList[j]
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        myList[i] = base
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList

myList = [53,18,32,17,123,93,45,54]
print("结果为: ",QuickSort(myList,0,len(myList)-1))
