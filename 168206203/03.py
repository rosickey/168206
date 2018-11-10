# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def q_sort(array,low,high):
    if high-low<=1:
        return array

    pivokey=array[low]
    i=low
    j=high-1
    while i<j:
        while array[j]>pivokey and i<j:
            j=j-1
        else:
            array[i]=array[j]
        while array[i]<=pivokey and i<j:
            i=i+1
        else:
            
            array[j]=array[i]
            
    array[i]=pivokey
    
    q_sort(array, low, i)
    q_sort(array, i+1, high)
    return array
array=[2,2,5,2,52,8,2]
print("before q_sort=",array)
q_sort(array,0,len(array))
print("after q_sort=",array)

