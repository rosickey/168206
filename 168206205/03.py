# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:06:38 2018

@author: asus
"""

def fa(num):

    if num<3:

        return 1

    else:

        return fa(num-1)+fa(num-2)

for i in range(1,30):

    print(fa(i),end = ' ')