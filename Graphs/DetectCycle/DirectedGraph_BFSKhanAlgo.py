#We can't use the parent tracking method as used in undirected graph
#We will use the BFS Khan's Topo Algo

#If the topological sort path is not the size of number of vertices
#then there is cycle

def checkCycle():
    q = deque()
    res=[]
    for i in range(1,v+1):
        if inDeg[i]==0:
            q.append(i)

    while q:
        node = q.popleft()
        res.append(node)
        for nei in adj[node]:
            inDeg[nei]-=1
            if inDeg[nei]==0:
                q.append(nei)
    if len(res)==v: return False
    return True

#Directed Graph
edges = [(1,2),(2,3),(3,4),(4,5),(5,6),(3,7),(7,5),(8,9),(9,10),(10,8),(8,2)]
v = 10
inDeg=[0 for _ in range(v+1)]
adj = defaultdict(list)
for src,dest in edges:
    adj[src].append(dest)
    inDeg[dest]+=1

if checkCycle(): print("Cycle Detected")
else: print("There is no Cycle")
