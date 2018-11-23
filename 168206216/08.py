# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 17:23:54 2018

@author: 李金印

换钢琴问题
"""

#构建图，用于遍历
graph1={}
graph1=["乐谱"]={}
graph1=["乐谱"]["唱片"]=5
graph1=["乐谱"]["海报"]=0
graph1=["唱片"]={}
graph1=["唱片"]["吉他"]=15
graph1=["唱片"]["架子鼓"]=20
graph1=["海报"]={}
graph1=["海报"]["吉他"]=30
graph1=["海报"]["架子鼓"]=35
graph1=["吉他"]={}
graph1=["吉他"]["钢琴"]=20
graph1=["架子鼓"]={}
graph1=["架子鼓"]["钢琴"]=10
graph1=["钢琴"]={}

#记录金钱开销
costs={}
infinity=float("inf")
costs["乐谱"]
