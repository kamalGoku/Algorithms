class TrajanAlgorithm:
    def __init__(self,v, edges):
        self.adj = defaultdict(list)
        self.V = v
        self.inTime = [0 for _ in range(v+1)]
        self.low = [sys.maxsize for _ in range(v+1)]
        self.bridges = []
        self.visited = [False for _ in range(v+1)]
        self.timer = 1
        self.__buildAdjList(edges)
    
    def __buildAdjList(self, edges):
        for src,dest in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

    def findCriticalPaths(self,start,parent):
        self.visited[start] = True
        #Initially, the low and inTime will be running timer
        self.inTime[start]    = self.timer
        self.low[start]     = self.timer
        #Incrementing the timer
        self.timer+=1
        for nei in self.adj[start]:
            #don't include logic for parent
            if nei==parent: continue
            if self.visited[nei]==False:
                #if the neighboring node is not visited, recurse
                self.findCriticalPaths(nei,start)
                #After neighbour completes the recursion, 
                #compare the low times of neighbour
                #if the neighbour's low time is < curr node then update it
                self.low[start] = min(self.low[nei], self.low[start])
                
                #if the neighbours low time is greater then the curr node's inTime
                #then it is a bridge, removing it will disconnect the graph
                if self.inTime[start]<self.low[nei]:
                    self.bridges.append((start,nei))
            else:
                #if the neighbours node is already visited
                #then update the low time of current with neighbours inTime
                self.low[start] = min(self.inTime[nei], self.low[start])
    
    def printBridges(self):
        for bridge in self.bridges:
            print(bridge)

edges = [(1,2),(1,4),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(6,9),(8,9),(8,10),(10,11),(10,12),(11,12)]
V = 12
tA = TrajanAlgorithm(V, edges)
tA.findCriticalPaths(1,-1)
tA.printBridges()
    
