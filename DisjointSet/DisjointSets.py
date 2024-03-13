class DisjointSet:
    def __init__(self, n):
        #Initialized with n+1 to have both 0 based and 1 based indexing
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)]
        self.size = [1 for _ in range(n+1)]
    
    #Time comp: O(logn) without path compression
    def findParent(self, u):
        if self.parent[u]==u:
            return u
        #Path compression to update the ultimate parents
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]
    
    #Union by rank doesn't increase rank after merging which is bit confusing
    #Better to use union by size
    def unionByRank(self, u, v):
        uParent = self.findParent(u)
        vParent = self.findParent(v)
        if uParent==vParent: return
        if self.rank[uParent]>self.rank[vParent]:
            self.parent[vParent]=uParent
        elif self.rank[uParent]<self.rank[vParent]:
            self.parent[uParent]=vParent
        else:
            self.parent[vParent]=uParent
            self.rank[uParent]+=1
    
    #Keeps track of set sizes
    def unionBySize(self, u, v):
        #Find ultimate parents
        uParent = self.findParent(u) 
        vParent = self.findParent(v)
        #return if both have same parents
        if uParent==vParent: return
        if self.size[uParent]<self.size[vParent]:
            self.parent[uParent]=vParent
            self.size[vParent]+=self.size[uParent]
        else: #greater than and equal case
            self.parent[vParent]=uParent
            self.size[uParent]+=self.size[vParent]

#Creating a set with 7 nodes
g = DisjointSet(7)
g.unionBySize(1,2)
g.unionBySize(2,3)
g.unionBySize(4,5)
g.unionBySize(6,7)
g.unionBySize(5,6)

#if 3 and 7 same or not 
if g.findParent(3) == g.findParent(7): print("In Same Set")
else: print("NOT in Same Set")

g.unionBySize(3,7)

#if 3 and 7 same or not 
if g.findParent(3) == g.findParent(7): print("In Same Set")
else: print("NOT in Same Set")
