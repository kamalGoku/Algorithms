#Find the shortest path from Source to other nodes using Topological Sorting. 
#Applicable only for DAG
#Intuition: We visit all the nodes and compute the cost before the next node.
#Overall TC: O(V+E)

#Find the Shortest path by removing nodes from the topo path
def findShortestPath(source):
    dist[source]=0
    while topoPath:
        temp = topoPath.pop()
        for nei,wt in adj[temp]:
            if dist[temp]+wt<dist[nei]:
                dist[nei]=dist[temp]+wt
        
#Function to find the topological sort of given graph
def topoSort(start):
    visited[start]=True
    for nei,wt in adj[start]:
        if not visited[start]:
            topoSort(nei)
    topoPath.append(start)
    
#Directed Graph(src,dest,wt)
edges = [(6,5,3),(6,4,2),(5,4,1),(4,0,3),(4,2,1),(0,1,2),(2,3,3),(1,3,1)]
v = 7
adj = defaultdict(list)
visited = [False for _ in range(v)]
topoPath = []
dist = [sys.maxsize for _ in range(v)]
for src,dest,wt in edges:
    adj[src].append((dest,wt))
    
#Find the topoPath
for i in range(v):
    if not visited[i]:
        topoSort(i)

#Find Shortest path from Source
findShortestPath(6) #SourceNode is 6

print("Distance Array: ", dist)
