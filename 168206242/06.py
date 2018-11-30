
infinity=float("inf")
graph={}#定义散列表
graph["yp"]={}
graph["yp"]["hb"]=0
graph["yp"]["cp"]=5

graph["cp"]={}
graph["cp"]["jt"]=15
graph["cp"]["jzg"]=20

graph["hb"]={}
graph["hb"]["jt"]=30
graph["hb"]["jzg"]=35

graph["jt"]={}
graph["jt"]["gq"]=20

graph["jzg"]={}
graph["jzg"]["gq"]=10
 

costs={}#定义cost表
costs["hb"]=0
costs["cp"]=5
costs["jt"]=infinity
costs["jzg"]=infinity
costs["gq"]=infinity
 
parents={}#定义父表
parents["hb"]="yp"
parents["cp"]="yp"
parents["jt"]=None
parents["jzg"]=None
parents["gq"]=None
processed=[]#存储处理过的路径
 
def find_lowest_cost_node(costs):#找出最低开销节点
     lowest_cost=float("inf")
     lowest_cost_node=None
     for node in costs:
         cost=costs[node]
         if cost<lowest_cost and node not in processed:
             lowest_cost=cost
             lowest_cost_node=node
     return lowest_cost_node
 

def breadth_first_search(costs):#核心算法
     node=find_lowest_cost_node(costs)
     while node is not None:
         cost=costs[node]
         neighbors=graph.get(node)
         for n in neighbors.keys():
             a_cost = neighbors.get(n)
             new_cost=cost+a_cost
             if costs[n]>new_cost:
                 costs[n]=new_cost
                 parents[n]=node
         processed.append(node)
         node=find_lowest_cost_node(costs)
         if node not in graph:
                break
         print(new_cost)
         



def shortest_path_search():#计算最短路径
    node="gq"
    shortest_path=["gq"]
    while parents[node] is not "yp":
        shortest_path.append(parents[node])
        node=parents[node]
    shortest_path.append("yp")
    return shortest_path

breadth_first_search(costs)
print(costs)#路径的开销
print(parents)#所有路径的父类子类关系
print(shortest_path_search())#经过的路径.
