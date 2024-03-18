#BELMAN FORD ALGORITHM
#Applicable on on Directed Graph
#Used when edge cost is negative and negative cycles

#Intuition: Update the distance matrix V-1 times, where V is num of vertices
#all the paths cost will be calcualted in V-1 times

#Overall TC: O(VE)

def bellmanFordShortest(source):
    dist[source]=0
    for _ in range(V-1): #Executed for V-1 times
        for src,dest,wt in edges: #For all edges
            if dist[src]!=sys.maxsize: #Only if the vertex is visited
                if dist[dest]>dist[src]+wt:
                    dist[dest]=dist[src]+wt
        
#Undirected Graph weights(src,dest,wt)
edges = [(1,2,-2),(2,4,3),(0,1,5),(1,5,-3),(3,2,6),(3,4,-2),(5,3,1)]
V = 6
dist = [sys.maxsize for _ in range(V)]

#Find Shortest path from Source
bellmanFordShortest(0) #SourceNode is 0

print("Distance Array: ", dist)
