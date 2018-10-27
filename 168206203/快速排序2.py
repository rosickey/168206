# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:32:35 2018

@author: Yan
"""
"""快速排序"""

def Q_sort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less =[i for i in array[1:] if i<=pivot]
        greater=[i for i in array[1:] if i>pivot]
        return Q_sort(less)+[pivot]+Q_sort(greater)
array=[3,5,8,5,156,8,0]
print(Q_sort(array))
