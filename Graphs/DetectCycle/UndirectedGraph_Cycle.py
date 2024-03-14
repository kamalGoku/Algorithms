
#We keep track of the parent to check from where we come from

#Using DFS
def dfs(start,parent):
    visited[start] = True
    for nei in adj[start]:
        if visited[nei]==False:
            if dfs(nei, start):
                return True
        elif nei!=parent:
            #if we see any other node other than our parent then there is loop
            return True
    return False

#using BFS
def bfs(start):
    q = deque()
    q.append((start,-1))
    while q:
        qLen=len(q)
        for _ in range(qLen):
            node,parent = q.popleft()
            visited[node]=True
            for nei in adj[node]:
                if visited[nei]==False:
                    q.append((nei,node))
                elif nei!=parent:
                    #if we see any other node other than our parent then there is loop
                    return True
    return False

edges = [(0,1), (1,2),(2,3),(3,4),(4,1)]
v = 5
adj = defaultdict(list)
for src,dest in edges:
    adj[src].append(dest)
    adj[dest].append(src)
visited = [False for _ in range(v)]
for node in range(v):
    if visited[node]==False:
        if dfs(node,-1):
            print("Loop detected")
        #if bfs(node):
        #    print("Loop Detected")
