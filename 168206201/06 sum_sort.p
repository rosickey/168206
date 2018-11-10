# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 21:00:00 2018

@author: 程甜甜
"""

def sun(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])
