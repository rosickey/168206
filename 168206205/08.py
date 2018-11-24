# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:18:47 2018

@author: asus
"""
#图的构建，各个节点之间的联系及权值
graph = {}
graph["yuepu"] = {}
graph["yuepu"] ["changpian"] = 5
graph["yuepu"] ["haibao"] = 0

graph["changpian"] = {}
graph["changpian"] ["jita"] = 15
graph["changpian"] ["jiazigu"] = 20

graph["haibao"] = {}
graph["haibao"]["jita"] = 30
graph["haibao"] ["jiazigu"] = 35

graph["jita"] = {}
graph["jita"]["gangqin"] = 20

graph["jiazigu"] = {}
graph["jiazigu"]["gangqin"] = 10

graph ["gangqin"] = {}

#创建开销表
infinity = float ("inf")#定义无穷

costs = {}
costs["changpian"] = 5
costs["haibao"] = 0
costs["jita"] = infinity     #将不知道的开销定义为无穷
costs["jiazigu"] = infinity
costs["gangqin"] = infinity

#创建父节点表
parents = {}
parents["changpian"] = "yuepu"
parents["haibao"] = "yuepu"
parents["jita"] =None
parents["jiazigu"] =None
parents["gangqin"] = None

processed = []   #用于存储处理过的节点

#寻找最低开销的节点
def find_lowest_cost_node(costs) :
    lowest_cost = float("inf")   #将初始开销定义为无穷
    lowest_cost_node = None    #最低开销节点
    for node in costs:     #遍历costs表中的所有节点
        cost = costs[node]    #更新cost值
        if cost < lowest_cost and node not in processed:   #如果该节点的开销更低且未处理过
            lowest_cost = cost  #将该节点的开销赋给最低开销
            lowest_cost_node = node   #将其视为最低开销节点
    return lowest_cost_node

#寻找最短路径
def find_shortest_path():
    node = "gangqin"   #将终点设置为钢琴
    shortest_path = ["gangqin"]  #用于存储最低开销所经过的节点
    while parents[node] != "yuepu":  #只要父节点不是乐谱则重复此动作
        shortest_path.append(parents[node])  #将该节点的父节点标记已处理
        node = parents[node]   #更新父节点
    shortest_path.append("yuepu")   #最后将乐谱节点加入列表
    return shortest_path

#寻找最低开销路径
def find_shortest_cost_path():
    node = find_lowest_cost_node(costs)  #在未处理的节点中寻找开销最小的节点
    while node is not None:  #所有节点都处理过后结束
        cost = costs[node]   #更新cost值，将开销最小的节点的cost值赋值给cost
        neighbors = graph[node]  #找到该节点的邻居
        for n in neighbors.keys():  #遍历当前节点所有邻居
            new_cost = cost + neighbors[n]   #更新cost值
            if costs[n] > new_cost:   #如果当前节点前往邻居处花费更少
                costs[n] = new_cost   #就更新该邻居开销
                parents[n] = node   #同时将该邻居的父节点设置为当前节点
        processed.append(node)    #并将该节点标志位已处理
        node = find_lowest_cost_node(costs)   #找出接下来要处理的节点并循环
    shortest_path = find_shortest_path()   #将找到的最短路径存放到列表
    shortest_path.reverse()   #将列表中的节点反向排序
    print ("最少花费%d美元可以用乐谱交换钢琴"%(new_cost))
    print("其交换路径为:")
    print(shortest_path)
    
find_shortest_cost_path()


