#User function Template for python3
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]
    
    def findParent(self, u):
        if self.parent[u]==u: return u
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]
        
    def unionBySize(self, u, v):
        uParent = self.findParent(u)
        vParent = self.findParent(v)
        if uParent==vParent: return
        if self.size[uParent]<self.size[vParent]:
            self.parent[uParent]=vParent
            self.size[vParent]+=self.size[uParent]
        else:
            self.parent[vParent]=uParent
            self.size[uParent]+=self.size[vParent]
        
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        edges = []
        for v in range(V):
            for nei in adj[v]:
                edges.append([nei[1],v,nei[0]])
        edges.sort()
        minWt=0
        g = DisjointSet(V)
        for edge in edges:
            wt = edge[0]
            u = edge[1]
            v = edge[2]
            if g.findParent(u)!=g.findParent(v):
                minWt+=wt
                g.unionBySize(u,v)
            
        return minWt
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends
