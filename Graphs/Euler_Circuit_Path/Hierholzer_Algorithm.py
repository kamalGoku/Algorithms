#HIERHOLZER'S ALGORITHM for finding the EULER PATH in a GRAPH

#For Undirected Graph, it it has a Eulerian Path then
# - Atmost one vertex should have inDeg-outDeg==1
# - Atmost one vertex should have outDeg-intDeg==1
# - All other vertices should have equal inDeg and OutDeg
# - If any vertex has |inDeg-outDeg| value more than 1 then it can't form an Eulerian Path
def checkForEuler():
    startNode = 0
    lastNode = 0
    for i in range(n):
        if abs(inDeg[i]-outDeg[i])>1:
            return False
        elif inDeg[i]-outDeg[i]==1:
            lastNode+=1
        elif outDeg[i]-inDeg[i]==1:
            startNode+=1
    
    return (startNode==0 and lastNode==0) or\
           (startNode==1 and lastNode==1)

#In the Graphs does not have an Eulerian circuit
#then start the path from
#  - the vertex which has more outDeg than inDeg
#  - or any vertex with non-zero outDeg
def getStartingNode():
    start = 0
    for i in range(n):
        if outDeg[i]-inDeg[i]==1:
            return i
        if outDeg[i]>1: start=i
    return start

#The edge should be visited only once, so remove it from adjList
#once all the neighbours are visted, add it to the path
def getEulerPath(start):
    while adj[start]:
        currNode = adj[start].pop()
        getEulerPath(currNode)
    eulerPath.append(start)
        
edges = [(0,1),(1,2),(2,1),(1,3),(3,4)]
n=5 #number of nodes
e = len(edges) #number of edges
adj = defaultdict(list)
inDeg = [0 for _ in range(n)]
outDeg = [0 for _ in range(n)]

#Create the Adjacency list and update the inDeg and OutDeg
for src, dest in edges:
    adj[src].append(dest)
    inDeg[dest]+=1
    outDeg[src]+=1

if not checkForEuler():
    print("Doesn't have Euler circuit or Euler Graph")
else:
    #Get the starting node
    start = getStartingNode()
    
    #compute the path
    eulerPath = []
    getEulerPath(start)

    if len(eulerPath) != e+1:
        #all are not in one component
        print("There is no Eulerian Path")
    else:
        print("Eulerian Path: ", end=' ')
        print(eulerPath[::-1])
