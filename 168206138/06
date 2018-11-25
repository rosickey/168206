'''graph'''
graph = {}
graph["yuepu"] = {}
graph["yuepu"]["changpian"] = 5
graph["yuepu"]["haibao"] = 0
graph["changpian"] = {}
graph["changpian"]["jita"] = 15
graph["changpian"]["jiazigu"] = 20
graph["haibao"] = {}
graph["haibao"]["jita"] = 30
graph["haibao"]["jiazigu"] = 35
graph["jita"] = {}
graph["jita"]["piano"] = 20
graph["jiazigu"] = {}
graph["jiazigu"]["piano"] = 10
graph["piano"] = {}

"""costs"""
infinity = float("inf")#定义infinity为无穷'''
costs = {}
costs["changpian"] = 5
costs["haibao"] = 0
costs["jita"] = infinity
costs["jiazigu"] = infinity
costs["piano"] = infinity

"""prenter"""
parents = {}
parents["cbangpian"] = "yuepu" 
parents["haibao"] = "yuepu"
parents["jita"] = None 
parents["jiazigu"] = None
parents["piano"] = None  

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
	neighbors =graph[node]
	for n in neighbors.keys():
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			print("start -> " + n + " 要走" + str(costs[n]) + "改为")
			costs[n] = new_cost
			parents[n] =node
		print("start -> " + n + " 要走" + str(costs[n]))
	processed.append(node)
	node = find_lowest_cost_node(costs)
for n,m in costs.items():
	print(n + " : " + str(m))
