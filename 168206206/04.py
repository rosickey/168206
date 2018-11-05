# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 18:36:17 2018

@author: 云龍
"""

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:]if i > pivot]
        return quicksort(less) + [pivot] +quicksort(greater)
    
print(quicksort([10,5,2,3]))
