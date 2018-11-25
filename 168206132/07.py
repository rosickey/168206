# -*- coding: utf-8 -*-
"""
Spyder Editor @ypx

This is a temporary script file.
"""

graph = {}  
graph["yuepu"] = {}
graph["yuepu"]["haibao"] = 5
graph["yuepu"]["heijiao"] = 0
graph["haibao"] = {}
graph["haibao"]["jita"] = 30
graph["haibao"]["jiazigu"] = 35
graph["heijiao"] = {}
graph["heijiao"]["jita"] = 15
graph["heijiao"]["jiazigu"] = 20
graph["jita"] = {}
graph["jita"]["gangqin"] = 20
graph["jiazigu"] = {}
graph["jiazigu"]["gangqin"] = 10
graph["钢琴"] = {}

infinity = float("inf")
costs = {}       
costs["haibao"] = 5
costs["heijiao"] = 0
costs["jita"] = infinity
costs["jiazigu"] = infinity
costs["gangqin"] = infinity
parents = {}       
parents["haibao"] = "yueopu"
parents["heijiao"] = "yuepu"
parents["jita"] = None
parents["jiazigu"] = None
parents["gangqin"] = None
processed = []      
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node
	node = find_lowest_cost_node(costs)
 while node is not None:     
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(costs)

 key = "gangqin"
L = ["gangqin"]
while True:				
	key = parents[key]
	L.append(key)
	if key == "yuepu":
		break
i = -1
print ("路线为：",end='')
for x in L:
	print (L[i],end='')
	if L[i] != "gangqin":
		print ("-->",end='')
