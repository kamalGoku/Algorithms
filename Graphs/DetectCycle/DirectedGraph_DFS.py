
#We can't use the parent tracking method as used in undirected graph
#We will use the recur array to keep track of recursion path

#Using DFS
def dfs(start):
    visited[start] = True
    recur[start]=True
    for nei in adj[start]:
        if visited[nei]==False:
            if dfs(nei):
                return True
        elif recur[nei]==True:
            #if we see any other node other than our parent then there is loop
            return True
    recur[start]=False
    return False

#Directed Graph
edges = [(1,2),(2,3),(3,4),(4,5),(5,6),(3,7),(7,5),(8,9),(9,10),(10,8),(8,2)]
v = 10
adj = defaultdict(list)
for src,dest in edges:
    adj[src].append(dest)

visited = [False for _ in range(v+1)]
recur=[False for _ in range(v+1)]
loop = False
for node in range(v):
    if visited[node]==False:
        if dfs(node):
            loop=True

if loop: print("Loop Detected")
else: print("There is no Loop")
