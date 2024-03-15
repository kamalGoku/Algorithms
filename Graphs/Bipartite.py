def dfs(start,col):
    color[start]=col
    for nei in adj[start]:
        #newCol = not col
        if color[nei]==-1:
            if dfs(nei, 1-col)==False:
                return False
        elif color[nei]==col:
            return False
    return True

def bfs(start):
    q = deque()
    q.append(start)
    color[start]=0
    while q:
        qLen = len(q)
        for _ in range(qLen):
            temp = q.popleft()
            for nei in adj[temp]:
                if color[nei]==-1:
                    color[nei]= 1 - color[temp]
                    q.append(nei)
                elif color[nei]==color[temp]:
                    return False
    return True
v=4
bipartite = True
#edges = [(0,2),(2,3),(3,1)] #Bipartite
edges = [(0,2),(2,3),(3,1),(0,3)] #Non Bipartite
color = [-1 for _ in range(v)]
adj = defaultdict(list)
for src,dest in edges:
    adj[src].append(dest)
    adj[dest].append(src)

for i in range(v):
    if color[i]==-1:
        if dfs(i,0)==False:
            bipartite = False
        #if bfs(i)==False:
        #    bipartite = False
if bipartite:
    print("Bipartite Graph")
else:
    print("Not Bipartite Graph")
            
