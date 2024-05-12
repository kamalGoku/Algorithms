class Node:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max = high
        self.left=None
        self.right=None

class IntervalTree:
    def __init__(self):
        self.root = None

    def __insert(self, root, interval):
        if root==None:
            return Node(interval[0], interval[1])
        if root.low > interval[0]:
            root.left = self.__insert(root.left, interval)
        else:
            root.right = self.__insert(root.right, interval)
        if root.high<interval[1]:
            root.max = interval[1]
        return root
    
    def insert(self, interval):
        self.root = self.__insert(self.root, interval)
            
    def __printTree(self, root):
        if not root:
            return
        self.__printTree(root.left)
        print("Node: Low =", root.low, "High =", root.high, "Max =", root.max)
        self.__printTree(root.right)
        
    def printTree(self):
        self.__printTree(self.root)

    def __isOverlap(self, root, interval):
        if not root:
            return False
        if (root.low < interval[0] and root.high > interval[0]) or \
           (root.low < interval[1] and root.high > interval[1]):
            return True
        if root.left and root.left.max>interval[0]:
            #the overlapping node can be in the left subtree
            return self.__isOverlap(root.left, interval)
        else:
            return self.__isOverlap(root.right, interval)

    def isOverlap(self, interval):
        return self.__isOverlap(self.root, interval)
    
           
    def groupIntervals(self):
        groups = []
        currGroup = []
        st = []
        curr = self.root
        prevEnd = -sys.maxsize
        while True:
            if curr:
                st.append(curr)
                curr=curr.left
            elif st:
                curr = st.pop()
                #interval logic
                if prevEnd>curr.low: #overlap
                    currGroup.append([curr.low, curr.high])
                    prevEnd = curr.high
                else:
                    if currGroup:
                        groups.append(currGroup)
                    prevEnd = curr.high
                    currGroup = [[curr.low, curr.high]]
                    
                curr = curr.right
            else:
                break
        if currGroup:
            groups.append(currGroup)
        return groups
                
        
it = IntervalTree()
it.insert([15, 20])
it.insert([10, 30])
it.insert([17, 19])
it.insert([5, 20])
it.insert([12, 15])
it.insert([30, 40])

it.printTree()

print("Is [6,10] have overlap? : ", it.isOverlap([6,10]))
print("Is [41,43] have overlap? : ", it.isOverlap([41,43]))

print(it.groupIntervals())
