#FLOYD WARSHALL ALGORITHM (Multi source Shortest path Algo)
#Applicable on both Directed and Undirected Graph
#Can be used with negative weights 
#Detects negative cycle

#Intuition: Visit nodes via all nodes
#           i--> j ===> i-->k + k-->j
#use Adjacency MATRIX for this

#Overall TC: O(VE)

def floydWarshall():
    for k in range(V):
        for i in range(V):
            for j in range(V):
                costMatrix[i][j] = min(costMatrix[i][j], costMatrix[i][k]+costMatrix[k][j])
        
#Directed Graph weights(src,dest,wt)
edges = [(0,1,2),(1,0,1),(1,2,3),(3,0,3),(3,2,4),(3,1,5)]#,(0,3,-4)
V = 4
costMatrix = [[sys.maxsize for _ in range(V)] for _ in range(V)]

for src,dest,wt in edges:
    costMatrix[src][dest] = wt

for i in range(V):
    costMatrix[i][i]=0

#Find Shortest path from Source
floydWarshall() #SourceNode is 0

#The COst from and to same node should always be 0.
#If the value goes <0 then there is a negative cycle
for i in range(V):
    if  costMatrix[i][i]!=0:
        print("Negative Cycle exits in Graph")
        
print("Cost Matrix: ", costMatrix)
