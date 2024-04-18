class BSTIterator:
    def __init__(self, root, rev):
        self.st = []
        self.reverse = rev
        self.pushAll(root)
        
    
    def pushAll(self, root):
        while root:
            self.st.append(root)
            if self.reverse:
                root=root.right
            else:
                root=root.left

    def hasNext(self):
        if self.st:
            return True
        return False
    
    def nextNode(self):
        if self.st:
            curr = self.st.pop()
        else:
            return -1
        if self.reverse:
            self.pushAll(curr.left)
        else:
            self.pushAll(curr.right)
        return curr.data

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.data, end=' ')
    printTree(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
printTree(root)
print("")
bi = BSTIterator(root, True)
print(bi.nextNode())
print(bi.nextNode())
print(bi.nextNode())
print(bi.nextNode())
print(bi.nextNode())
print(bi.nextNode())
print(bi.nextNode())
print(bi.hasNext())
