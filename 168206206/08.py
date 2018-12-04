# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 20:25:09 2018

@author: 云龍
"""

graph={}


graph["ChangPian"]={}
graph["ChangPian"]["JiTa"]=15
graph["ChangPian"]["JiaZiGu"]=20


graph["JiaZiGu"]={}
graph["JiaZiGu"]["GangQin"]=10


graph["HaiBao"]={}
graph["HaiBao"]["JiTa"]=30
graph["HaiBao"]["JiaZiGu"]=35


graph["YuePu"]={}
graph["YuePu"]["ChangPian"]=5
graph["YuePu"]["HaiBao"]=0


graph["JiTa"]={}
graph["JiTa"]["GangQin"]=20


graph["GangQin"]={}


infinity=float("inf")

costs={}
costs["HaiBao"]=0
costs["ChangPian"]=5
costs["JiTa"]=infinity
costs["JiaZiGu"]=infinity
costs["GangQin"]=infinity


parents={}
parents["ChangPian"]="YuePu"
parents["HaiBao"]="YuePu"
parents["JiTa"]="None"
parents["JiaZiGu"]="None"
parents["GangQin"]="None"


           
def find_shortest_path():
    node='GangQin'
    shortest_path=["GangQin"]
    while node!="YuePu":
        node=parents[node]
        shortest_path.append(node)
    shortest_path.reverse()
    print('\n到达终点的最终路径：')
    print(shortest_path) 
      
processed=[]

def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for node in costs:  #遍历所有节点
        cost=costs[node]
        if cost<lowest_cost and node not in processed:  #如果当前节点开销更低且未处理过
            lowest_cost=cost                            #就将其视为开销最低的节点
            lowest_cost_node=node
    return lowest_cost_node


if __name__ == '__main__':
    node=find_lowest_cost_node(costs)   
    while node is not None:
        cost=costs[node]
        neighbors=graph[node]
        for n in neighbors.keys():
            new_cost=cost+neighbors[n]
            if costs[n]>new_cost:
                costs[n]=new_cost
                parents[n]=node
        processed.append(node) 
        node=find_lowest_cost_node(costs)
    shortest_path=find_shortest_path()
    print(shortest_path)

    