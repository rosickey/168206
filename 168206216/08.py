# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 17:23:54 2018

@author: 李金印

换钢琴问题
"""

#构建关系图，用于遍历
graph1 = {}
graph1["乐谱"] = {}
graph1["乐谱"]["唱片"] = 5
graph1["乐谱"]["海报"] = 0
graph1["唱片"] = {}
graph1["唱片"]["吉他"] = 15
graph1["唱片"]["架子鼓"] = 20
graph1["海报"] = {}
graph1["海报"]["吉他"] = 30
graph1["海报"]["架子鼓"] = 35
graph1["吉他"] = {}
graph1["吉他"]["钢琴"] = 20
graph1["架子鼓"] = {}
graph1["架子鼓"]["钢琴"] = 10
graph1["钢琴"] = {}

#构建开销表，从起点（乐谱）到每个结点需要的开销（infinity 无穷大）
costs = {}
infinity = float("inf")
costs["唱片"] = 5
costs["海报"] = 0
costs["吉他"] = infinity
costs["架子鼓"] = infinity
costs["钢琴"] = infinity

#构建存储父节点信息的散列表
parent = {}
parent["唱片"] = "乐谱"
parent["海报"] = "乐谱"
parent["吉他"] = None
parent["架子鼓"] = None
parent["钢琴"] = None

filter1 = []

#找到开销最小的节点
def find_low_cost_node(cost):
    low_cost = float("inf") #定义一个最大值
    low_node = None
    for node in costs :
        cost = costs[node]
        if(cost<low_cost and node not in filter1) :
            low_cost = cost
            low_node = node
    return low_node


node = find_low_cost_node(costs)

while node is not None :
    cost = costs[node]  #获取最小开销
    neighbors = graph1[node]    #获取最小开销的邻居节点
    for n in neighbors.keys() :
        new_cost = cost + neighbors[n]  #走向该节点的开销
        if(costs[n] > new_cost) :   #判断从起点走到n节点的开销是否比直接从起点到n的开销小
            costs[n] = new_cost     #如果小，更新开销表
            parent[n] = node        #更新流程 乐谱->node->n ,记录父节点
    filter1.append(node)            #已经判断过node了，加入过滤器，在选择当前开销表最小开销时过滤这个点，否则会无限循环
    node = find_low_cost_node(cost)
    

#递归整个流程
def get_course(sign) :
    if(sign != "乐谱") :
        return get_course(parent[sign]+" --> "+sign)
    else :
        return sign
print(get_course("钢琴"))
