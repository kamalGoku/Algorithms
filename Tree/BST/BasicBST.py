class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def __insert(self, node, val):
        if not node:
            return Node(val)
        if node.data<val:
            node.right = self.__insert(node.right,val)
        elif node.data>val:
            node.left = self.__insert(node.left,val)
        return node
            
    def insert(self, val):
        self.root = self.__insert(self.root, val)
    
    def __printTree(self, node):
        if not node: return
        self.__printTree(node.left)
        print(node.data, end=' ')
        self.__printTree(node.right)
    
    def printTree(self):
        print("Tree:=====", end=' ')
        self.__printTree(self.root)
        
    def __findLastRight(self, node):
        if not node.right:
            return node
        return self.__findLastRight(node.right)

    def __deleteUtil(self, node):
        if not node.left and not node.right: #LeafNode
            return None
        elif not node.left: #left if NULL
            return node.right
        elif not node.right: #right is NULL
            return node.left
        else:
            lastRight = self.__findLastRight(node.left)
            lastRight.right = node.right
            return node.left
        
    def __delete(self, node, val):
        if node.data<val:
            node.right = self.__delete(node.right, val)
        elif node.data>val:
            node.left = self.__delete(node.left, val)
        else:
            return self.__deleteUtil(node)
        return node

    def delete(self, val):
        self.root = self.__delete(self.root, val)

bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(1)
bst.insert(9)
bst.insert(7)
bst.insert(10)
bst.insert(6)
bst.printTree()
print("\n\n****Deleting Node 7")
bst.delete(7)
bst.printTree()
print("\n\n****Deleting Node 9")
bst.delete(9)
bst.printTree()
print("\n\n****Deleting Node 10")
bst.delete(10)
bst.printTree()
print("\n\n****Deleting Node 5 - the ROOT")
bst.delete(5)
bst.printTree()
print("\n\n****Inserting Node 5 again")
bst.insert(5)
bst.printTree()
