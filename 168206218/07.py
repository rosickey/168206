processed = []
infinity = float("inf")
graph = {}
graph["YuePu"] = {}
graph["YuePu"]["ChangPian"] = 5
graph["YuePu"]["HaiBao"] = 0
graph["ChangPian"] = {}
graph["ChangPian"]["JiTa"] = 15
graph["ChangPian"]["JiaZiGu"] = 20
graph["HaiBao"] = {}
graph["HaiBao"]["JiTa"] = 30
graph["HaiBao"]["JiaZiGu"] = 35
graph["JiTa"] = {}
graph["JiTa"]["GangQin"] = 20
graph["JiaZiGu"] = {}
graph["JiaZiGu"]["GangQin"] = 10
graph["GangQin"] = {}

costs = {}
costs["ChangPian"] = 5
costs["HaiBao"] = 0
costs["JiTa"] = infinity
costs["JiaZiGu"] = infinity
costs["GangQin"] = infinity

parents = {}
parents["ChangPian"] = "YuePu"
parents["HaiBao"] = "YuePu"
parents["JiTa"] = None
parents["JiaZiGu"] = None
parents["GangQin"] = None

#  找最小节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 找最短路径
def find_shotest_path():
    node = "GangQin"
    shotest_path = ["GangQin"]
    while parents[node] != "YuePu":
        shotest_path.append(parents[node])
        node = parents[node]
    shotest_path.append("YuePu")
    return shotest_path


#  找最少加权花费
def find_lowest_cost():
    # 最小开销节点
    node = find_lowest_cost_node(costs)
    # 只要有最小开销节点就循环
    while node is not None:
        # 获取当前节点的开销
        cost = costs[node]
        # 获取该节点的相邻节点
        neighbors = graph[node]
        # 遍历这些相邻节点
        for n in neighbors:
            # 计算当前节点的开销及相邻节点到当前节点的开销
            new_cost = cost + neighbors[n]
            # 若计算后的开销比该节点当前的开销小，则更新该节点的开销及父节点
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        # 保存处理过的节点
        processed.append(node)
        # 查找下一个最小开销节点，若不存在则结束循环
        node = find_lowest_cost_node(costs)
    # 所有节点都处理完毕
    return new_cost

def the_shotest_path():
    shotest_path = find_shotest_path()
    shotest_path.reverse()
    for each in shotest_path:
        print("->", str(each), end = " ")


if __name__ == "__main__":
    print("乐谱换钢琴的最小花费是", str(find_lowest_cost()))
    print("换钢琴的最短路径为：", end = "")
    the_shotest_path()
