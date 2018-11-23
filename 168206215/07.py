#使用循环进行拓扑排序
def topoSort(G):
    #初始化计算被指向节点的字典
    cnt=dict((u,0) for u in G.keys())
    #若某节点被其他节点指向，该节点计算量+1
    for u in G:
        for v in G[u]:
            cnt[v]+=1
    #收集被指向数为0的节点,此时Q只有一个节点，即起始节点a
    Q=[u for u in cnt.keys() if cnt[u]==0]
    #记录结果
    seq=[]
    while Q:
        s=Q.pop()
        seq.append(s)
        for u in G[s]:
            cnt[u]-=1
            if cnt[u]==0:
                Q.append(u)
    return seq

#有向无环图的邻接字典
G={
    'a':{'b','f'},
    'b':{'c','d','f'},
    'c':{'d'},
    'd':{'e','f'},
    'e':{'f'},
    'f':{}
}

res=topoSort(G)
print(res)