#PRIMS ALGORITHM to find the Minimum Spanning tree(MST)
#Use minHeap to store the edge weights and vist them

#Time Complexity: O(E log E)

def primsMstAlgo(start):
    q = []
    mstWt = 0
    heappush(q, (0,0,-1))
    #E log E
    while q:
        currWt,node,parent = heappop(q)
        if visited[node]: continue #If the node is visited just skip****
        visited[node]=True
        mstWt+=currWt #Add the MST weight
        if parent!=-1:
            mstNodes.append((parent, node)) #Track the MST edges
        #E log E
        for nei,wt in adj[node]:
            if visited[nei]==False: #only if the neig is not visited
                heappush(q,(wt,nei,node))
    return mstWt


V=5
edges = [(0,1,2),(0,2,1),(1,2,1),(2,4,2),(2,3,2),(3,4,1)]
visited = [False for _ in range(V)]
adj = defaultdict(list)
mstNodes = []

for src,dest,wt in edges:
    adj[src].append((dest,wt))
    adj[dest].append((src,wt))

print("MST Wt: ", primsMstAlgo(0))
print(mstNodes)
