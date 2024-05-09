class Node:
    def __init__(self):
        self.word = ''
        self.left = None
        self.right = None
        self.len = 0

class RopeTree:
    def __init__(self, word):
        self.maxLen = 5
        self.root = self.buildTree(word, 0, len(word)-1)
    
    def buildTree(self, word, start, end):
        temp = Node()
        mid = (start+end)//2
        if end-start+1>self.maxLen:
            temp.left = self.buildTree(word, start, mid)
            temp.right = self.buildTree(word, mid+1, end)
            temp.len = temp.left.len+temp.right.len
            return temp
        else: #leafNode
            temp.word = word[start:end+1]
            temp.len = end-start+1
            return temp

    
    def __printTree(self, root):
        if not root:
            return
        if not root.left and not root.right:
            print(root.word)
        self.__printTree(root.left)
        self.__printTree(root.right)
        
    def printTree(self):
        self.__printTree(self.root)
    
    def __charAt(self, root, idx):
        if not root.left and not root.right:
            return root.word[idx]
        if idx>root.len:
            print("ERROR - out of bound")
            return 
        if idx<root.left.len:
            return self.__charAt(root.left, idx)
        else:
            return self.__charAt(root.right, idx-root.left.len)
        
    def charAt(self, idx):
        return self.__charAt(self.root, idx)
    

rt = RopeTree("This_is_a_very_complex_sentence")
rt.printTree()
idx = 3
print("Char at", idx, ":", rt.charAt(idx))
idx = 7
print("Char at", idx, ":", rt.charAt(idx))
idx = 15
print("Char at", idx, ":", rt.charAt(idx))
idx = 19
print("Char at", idx, ":", rt.charAt(idx))
idx = 56
print("Char at", idx, ":", rt.charAt(idx))
