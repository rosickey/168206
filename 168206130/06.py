# -*- coding: utf-8 -*- 
graph = {}       创建关系字典
graph["乐谱"] = {}
graph["乐谱"]["海报"] = 5
graph["乐谱"]["黑胶"] = 0
graph["海报"] = {}
graph["海报"]["吉他"] = 30
graph["海报"]["架子鼓"] = 35
graph["黑胶"] = {}
graph["黑胶"]["吉他"] = 15
graph["黑胶"]["架子鼓"] = 20
graph["吉他"] = {}
graph["吉他"]["钢琴"] = 20
graph["架子鼓"] = {}
graph["架子鼓"]["钢琴"] = 10
graph["钢琴"] = {}
#print(graph)
infinity = float("inf")
costs = {}       节点权值字典
costs["海报"] = 5
costs["黑胶"] = 0
costs["吉他"] = infinity
costs["架子鼓"] = infinity
costs["钢琴"] = infinity
parents = {}       #父亲节点字典
parents["海报"] = "乐谱"
parents["黑胶"] = "乐谱"
parents["吉他"] = None
parents["架子鼓"] = None
parents["钢琴"] = None
processed = []      空list存放已访问的节点
def find_lowest_cost_node(costs):   节点处理函数
	lowest_cost = float("inf")
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node
	node = find_lowest_cost_node(costs)

while node is not None:     访问没有被访问过的节点
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

key = "钢琴"
L = ["钢琴"]
while True:				#转换为list类型 然后倒序输出
	key = parents[key]
	L.append(key)
	if key == "乐谱":
		break
i = -1
print ("路线为：",end='')
for x in L:
	print (L[i],end='')
	if L[i] != "钢琴":
		print ("-->",end='')
	i = i-1
