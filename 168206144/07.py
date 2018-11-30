# -*- coding:utf-8 -*-
def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None  
    for node in costs: 
        cost = costs[node]
        if cost < lowest_cost and node not in processed: 
            lowest_cost = cost 
            lowest_cost_node = node 
    return lowest_cost_node

def lujing():
    graph = {"乐谱": {"黑胶唱片": 5, "海报": 0}, "黑胶唱片": {"低音吉他": 15,"架子鼓":20}, "海报": {"低音吉他": 30, "架子鼓":35}, "低音吉他":{"钢琴":20},"架子鼓":{"钢琴":10},"钢琴":{}}
    infinity = float("inf")
    costs = {"黑胶唱片": 5,"海报": 0,"低音吉他":20,"架子鼓":35,"钢琴": infinity}
    parents = {"黑胶唱片": "乐谱", "海报": "乐谱","低音吉他":None,"架子鼓":None,"fin": None}
    best_route = ""
    processed = []
    node = find_lowest_cost_node(costs, processed)    
    while node is not None: 
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost 
                parents[n] = node 
        processed.append(node) 
        node = find_lowest_cost_node(costs, processed) 
    p = parents["钢琴"]
    while True:  
        best_route += "%s<--" % p
        p = parents[p]
        if p is "乐谱":
            break
                          
    return "交换的最少支付路径为: 钢琴<——%s乐谱。\n最少消费为%s元" % (best_route, costs["钢琴"])


best_route = lujing()
print(best_route)
