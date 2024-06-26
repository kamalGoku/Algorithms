#KOSARAJU ALGORITHM
#Strongly connected components are valid only for DG(Directed Graphs)

#Do DFS and store the vertices in stack after visited all neighboring vertices
#Store the reverse edges in seperate adj list
#Take elements from stack and do reverse DFS, now if we can't find neigh nodes then
#end thats the connected component. Keep track of them
#Time Complexity: O(V+E)

def dfs(start,visited,st):
    visited[start]=True
    for nei in adj[start]:
        if visited[nei]==False:
            dfs(nei,visited,st)
    st.append(start)

def revDfs(start,visited):
    visited[start]=True
    for nei in revAdj[start]:
        if visited[nei]==False:
            revDfs(nei,visited)

def kosarajuAlgo():
    st = []
    scc = 0
    visited = [False for _ in range(V)]
    #O(V+E)
    for i in range(V):
        if visited[i]==False:
            dfs(i,visited,st)
    visited = [False for _ in range(V)]
    #O(V+E)
    while st:
        curr = st.pop()
        if visited[curr]==False:
            revDfs(curr,visited)
            scc+=1
    return scc

V=5
edges = [(1,0),(0,2),(2,1),(0,3),(3,4)]
adj = defaultdict(list)
revAdj = defaultdict(list)
for src,dest in edges:
    adj[src].append(dest)
    revAdj[dest].append(src)
    
print("Number of connected Components = ", kosarajuAlgo())
