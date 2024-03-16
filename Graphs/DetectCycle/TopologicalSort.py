#TOPOLOGICAL SORT is applicable only in directed Acyclic Graph(DAG)
#TC: O(V+E)

#Using DFS
def dfs(start):
    visited[start] = True
    for nei in adj[start]:
        if visited[nei]==False:
            dfs(nei)
    res.append(start)

#Using BFS(Khan's Algo)
def bfs():
    q = deque()
    for i in range(v):
        if inDeg[i]==0:
            q.append(i)
   
    while q:
        print(q)
        node = q.popleft()
        res.append(node)
        for nei in adj[node]:
            inDeg[nei]-=1
            if inDeg[nei]==0:
                q.append(nei)
          
        
#Directed Graph
edges = [(2,3),(3,1),(4,0),(4,1),(5,0),(5,2)]
v = 6
adj = defaultdict(list)
res = []
'''
inDeg = [0 for _ in range(v)]

for src,dest in edges:
    adj[src].append(dest)
    inDeg[dest]+=1

bfs()
print(res)
'''
#'''
visited = [False for _ in range(v+1)]
for node in range(v):
    if visited[node]==False:
        dfs(node)
print(res[::-1])
#'''
