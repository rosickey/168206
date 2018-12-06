def tuopu(graph): 
in_degrees = dict((u,0) for u in graph)
vertex_num = len(in_degrees) 

for u in graph: 
for v in graph[u]: 
in_degrees[v] += 1  #计算每个顶点的入度 
Q = [u for u in in_degrees if in_degrees[u] == 0] 
Seq = [] 
while Q: 
u = Q.pop()  
Seq.append(u) 
for v in graph[u]: 

in_degrees[v] -= 1   
if in_degrees[v] == 0: 
Q.append(v)    
if len(Seq) == vertex_num:  
return Seq 
else: 
print("there's a circle.") 

G = { 
'a':'bf', 
'b':'cdef', 
'c':'d', 
'd':'ef', 
'e':'',  #'e':'f', 
 'f':'e' 
} 
print(tuopu(G))  
