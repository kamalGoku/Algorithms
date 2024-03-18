#DIJKTRA's ALGORITHM
#Using Priority queue tomsolve which is efficient than normal queue

#Find shortest path from source to all other nodes
#Doesn't work for negative value paths and negative cycles
#Can't detect cycles

#Overall TC: O(ElogV)
#DFS
def dfs(source):
    q=[]
    heappush(q,(0,0))
    dist[source]=0
    while q:
        oldWt,node = heappop(q)
        for nei,wt in adj[node]:
            if dist[nei]>dist[node]+wt:
                dist[nei]=dist[node]+wt
                heappush(q,(dist[nei],nei))
        
#Undirected Graph weights(src,dest,wt)
edges = [(0,1,4),(0,2,4),(1,2,2),(2,3,3),(2,4,1),(2,5,6),(3,5,2),(4,5,3)]
v = 6
adj = defaultdict(list)
dist = [sys.maxsize for _ in range(v)]
for src,dest,wt in edges:
    adj[src].append((dest,wt))
    adj[dest].append((src,wt))

#Find Shortest path from Source
dfs(0) #SourceNode is 0

print("Distance Array: ", dist)
