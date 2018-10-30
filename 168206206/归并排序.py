# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:06:46 2018

@author: 云龍
"""

def merge_sort( list ):
    if len(list) == 1:
        return list
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    ll = merge_sort( left )
    rl =merge_sort( right )
    return merge(ll , rl)

def merge( left , right ):
    result = []
    while len(left)>0 and len(right)>0 :
        if left[0] <= right[0]:
            result.append( left.pop(0) )
        else:
            result.append( right.pop(0) )
    result += left
    result += right
    return result

list = [5,24 ,14 ,22 ,6]
print(merge_sort(list))
