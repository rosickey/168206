# -*- coding: utf-8 -*- 

graph = {}       
graph["yp"] = {}
graph["yp"]["hb"] =0
graph["yp"]["hj"] = 5 

graph["hb"] = {}
graph["hb"]["jt"] = 30
graph["hb"]["jzg"] = 35

graph["hj"] = {}
graph["hj"]["jt"] = 15
graph["hj"]["jzg"] = 20

graph["jt"] = {}
graph["jt"]["gq"] = 20

graph["jzg"] = {}
graph["jzg"]["gq"] = 10

graph["gq"] = {}

#print(graph)
infinity = float("inf")
costs = {}      
costs["hb"] = 5
costs["hj"] = 0
costs["jt"] = infinity
costs["jzg"] = infinity
costs["gq"] = infinity

parents = {}       
parents["hb"] = "yp"
parents["hj"] = "yp"
parents["jt"] = None
parents["jzg"] = None
parents["gq"] = None

processed = []      
def find_lowest_cost_node(costs):   
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
  
 #print (parents)
 key = "gq"
L = ["gq"]
while True:			
	key = parents[key]
	L.append(key)
	if key == "yp":
		break
i = -1
print ("最终路线：",end='')
for x in L:
	print (L[i],end='')
	if L[i] != "gq":
		print ("-->",end='')
	
