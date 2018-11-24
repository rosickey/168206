#coding=utf-8
#狄克斯特拉算法
#乐谱换钢琴问题

graph = {}
graph ["yuepu"] = {}
graph ["yuepu"]["changpian"] = {5}
graph ["yuepu"]["haibao"] = {0}

graph ["cahngpian"] ={}
graph ["cahngpian"]["jita"] ={15}
graph ["cahngpian"]["jiazigu"] ={20}

graph ["haibao"] = {}
graph ["haibao"]["jita"] = {30}
graph ["haibao"]["jiazigu"] = {35}

graph ["jita"] = {}
graph ["jita"]["gangqin"] = {20}

graph ["jiazigu"] = {}
graph ["jiazigu"]["gangqin"] = {10}

infinity = float("inf")
costs = {}
costs ["changpian"] = 5
costs ["haibao"] = 0

costs ["changpian"]= {}
costs ["changpian"]["jita"] = 15
costs ["changpian"]["jiazigu"] = 20

costs ["haibao"]= {}
costs ["haibao"]["jita"] = 30
costs ["haibao"]["jiazigu"] = 35

costs ["jita"]= {}
costs ["jita"]["gangqin"] = 20

costs ["jiazigu"]= {}
costs ["jiazigu"]["gangqin"] = 10

parents = {}
parents ["changpian"] = "yuepu"
parents ["haibao"] = "yuepu"
parents ["jita"] = "changpian"+"haibao"
parents ["jiazigu"] = "changpian"+"haibao"
parents ["gangqin"] = "jita"+"jiazigu"

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

'''def find_lowest_cost_node(costs)

    cost +costs[node]
    neighbors = graph[node]
    for n in neighbor.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)'''
