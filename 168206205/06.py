# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 21:01:04 2018

@author: asus
"""

def sum(list):
    if list == []: #数列为空
        return 0
    return list[0] + sum(list[1:])

print("sum=",sum([2,4,6,8]))