#Find Shortest path in undirected graph with unit weights
#Just apply plain BFS

#Overall TC: O(V+E)
#Find the Shortest path by BFS
def bfs(source):
    q=deque()
    q.append(source)
    dist[source]=0
    while q:
        temp = q.popleft()
        for nei in adj[temp]:
            if dist[temp]+1<dist[nei]:
                dist[nei]=dist[temp]+1
                q.append(nei)
        
#Undirected Graph with unit weights(src,dest)
edges = [(0,1),(0,3),(1,2),(3,4),(4,5),(5,6),(2,6),(6,7),(6,8),(7,8)]
v = 9
adj = defaultdict(list)
dist = [sys.maxsize for _ in range(v)]
for src,dest in edges:
    adj[src].append(dest)
    
#Find Shortest path from Source
bfs(0) #SourceNode is 0

print("Distance Array: ", dist)
