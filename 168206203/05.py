# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 18:36:15 2018

"""
def sum(list):
  
     if list==[]:
         return 0;
     return list[0]+sum(list[1:])
     
list=[1,2,5,2,8]
print(sum(list))
