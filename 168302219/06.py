#graph表
graph={}
graph["yuepu"]={}
graph["yuepu"]["changpian"]=5
graph["yuepu"]["haibao"]=0

graph["changpian"]={}
graph["changpian"]["jita"]=15
graph["changpian"]["jiazigu"]=20

graph["haibao"]={}
graph["haibao"]["jita"]=30
graph["haibao"]["jiazigu"]=35

graph["jita"]={}
graph["jita"]["gangqin"]=20

graph["jiazigu"]={}
graph["jiazigu"]["gangqin"]=10

graph["gangqin"]={}

#costs表
infinity=float("inf")
costs={}
costs["changpian"]=5
costs["haibao"]=0
costs["jita"]=infinity
costs["jiazigu"]=infinity
costs["gangqin"]=infinity

#parents表
parents={}
parents["changpian"]="yuepu"
parents["haibao"]="yuepu"
parents["jita"]=None
parents["jiazigu"]=None
parents["gangqin"]=None

#processed数组，用于记录处理过的节点
processed=[]

# 找到开销最低的节点
def find_lowest_cost_node(costs):
    lowest_cost=float("inf") #将节点开销初值设为无穷
    lowest_cost_node=None  
    for node in costs:  #遍历所有节点
        cost=costs[node]
        if cost <lowest_cost and node not in processed: #若当前节点开销更低且未处理过
            lowest_cost=cost #将当前节点的开销视为最低开销
            lowest_cost_node=node
    return lowest_cost_node

# 找到支付额外费用最少的路径
def find_shortest_path():
	node = "gangqin"
	shortest_path = ["gangqin"]
	while parents[node] != "yuepu":
		shortest_path.append(parents[node])
		node = parents[node]
	shortest_path.append("yuepu")
	return shortest_path

def dijkstra():
    print('graph表：',graph)
    print('costs表：',costs)
    print('parents表：',parents)
    node=find_lowest_cost_node(costs)#找到未处理的节点中开销最少的节点
    while node is not None:  #在所有节点被处理过后结束
        cost=costs[node]
        neighbors=graph[node]
        for n in neighbors.keys(): #遍历当前节点的所有邻居
            new_cost=cost+neighbors[n]
            if costs[n]>new_cost: #如果计算后的开销比原本的开销少
                costs[n]=new_cost  #更新开销
                parents[n]=node   #将当前节点设为邻居的父节点
        processed.append(node) #将当前节点标记为已处理
        node=find_lowest_cost_node(costs)
    shortest_path = find_shortest_path()
    shortest_path.reverse()  #对shortest_path表里的元素反向排序，输出开销最少的路径
    print('更新后的costs表：',costs)
    print('更新后的parents表：',parents)
    print('支付额外费用最少的路径：',shortest_path)


# 测试
dijkstra()
