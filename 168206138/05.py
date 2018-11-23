"""
由AOV网构造拓扑序列的拓扑排序算法主要是循环执行以下两步，直到不存在入度为0的顶点为止。

(1) 选择一个入度为0的顶点并输出之;

(2) 从网中删除此顶点及所有出边。

循环结束后，若输出的顶点数小于网中的顶点数，则输出"有回路"信息，否则输出的顶点序列就是一种拓扑序列。
"""
'''
def topsort(G):
    in_degree = dict((x, 0) for x in G)
    for x in G:
        for y in G[x]:
            in_degree[y] += 1
    Q = [x for x in G if in_degree[x] == 0]
    S = []
    while Q:
        x = Q.pop()
        S.append(x)
        for i in G[x]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                Q.append(i)
    return S
G = {
    'a':'bf',
    'b':'cdf',
    'c':'d',
    'd':'ef',
    'e':'f',
    'f':''
}
print(topsort(G))
'''
def indegree0(v,e): 
 	if v==[]:
 		return None
 	tmp=v[:]
 	'''寻找入度为0的，放在tmp中'''
 	for i in e:
 		if i[1] in tmp:
 			tmp.remove(i[1])
 	if tmp==[]:
 		return -1
 	'''删除入度为0 的链接线'''
 	for t in tmp:
 		for i in range(len(e)):
 			if t in e[i]:
 				e[i]='toDel' #占位，之后删掉
 		#tmp.remove(t)
 	
 	if e:
 		eset=set(e)
 		eset.remove('toDel')
 		e[:]=list(eset)
 	
 	if v:
 		for t in tmp:
 			v.remove(t)
 	
 	return tmp
def topoSort(v,e):
 	result=[]
 	while True:
 		nodes=indegree0(v,e)
 		if nodes==None:
 			break
 		elif nodes==-1:
 			print('there\'s a circle.')
 			return None
 		result.extend(nodes)
 	return result
v=['a','b','c','d','e']
e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]
res=topoSort(v,e)
print(res)
