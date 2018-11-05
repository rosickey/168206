# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:20:43 2018

@author: 云龍
"""

def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

list=[3,1,14,36]
print(sum(list))
