#SEGMENT TREE
#used for range queries, 
#The array updates and queries will take max of O(logN)
#For 'n' queries, the TC will be nlogN

#This is done for finding maximum in the interval l-r

class SegmentTree:
    def __init__(self, n, inputArr):
        self.N=n #size fo array
        self.arr=inputArr #Copy the input array
        #Segment tree size can be 4 times the size of given array
        self.segTree = [0 for _ in range(4*self.N)]
        self.lazy = [0 for _ in range(4*self.N)]

    #Builds the SegmentTree
    #TC: O(logN)
    def buildST(self):
        self.__buildSTUtil(0,0,self.N-1)
    
    #Searches the ST
    #TC: O(logN)
    def query(self, l, r):
        return self.__queryUtil(0,0,self.N-1,l,r)
    
    #Update the specific index
    def updateIdx(self, idx, value):
        self.__updateIdxUtil(0,0,self.N-1,idx, value)
            
    #Update the given range with the value 
    #Lazy propagation
    def updateRange(self, l, r, value):
        self.__updateRangeUtil(0,0,self.N-1, l, r, value)
        
    #Prints the Segment Tree
    def printST(self):
        print(self.segTree)

    #Private functions not accessed outside
    def __buildSTUtil(self,segIdx,low,high):
        if low==high:
            self.segTree[segIdx]=self.arr[low]
            return
        mid = (low+high)//2
        self.__buildSTUtil(2*segIdx+1,low,mid)
        self.__buildSTUtil(2*segIdx+2,mid+1,high)
        self.segTree[segIdx] = max(self.segTree[2*segIdx+1], self.segTree[2*segIdx+2])
    
    #Util function to query the array with l-r
    def __queryUtil(self, segIdx, low, high, l, r):
        #Lies completely in range
        if low>=l and high<=r:
            return self.segTree[segIdx]
        #Lies outside range
        if high<l or low>r:
            return -sys.maxsize
        mid=(low+high)//2
        #partially in range
        leftVal = self.__queryUtil((2*segIdx)+1, low, mid, l, r)
        rightVal = self.__queryUtil((2*segIdx)+2, mid+1, high, l, r)
        return max(leftVal,rightVal)

    #Util function to update the index
    def __updateIdxUtil(self, segIdx, low, high, idx, value):
        #Lies outside range
        if idx>high or idx<low:
            return
        #Lies completely in range
        if low==idx and high==idx :
            self.segTree[segIdx] += value
            return

        mid=(low+high)//2
        #partially in range
        self.__updateIdxUtil((2*segIdx)+1, low, mid, idx, value)
        self.__updateIdxUtil((2*segIdx)+2, mid+1, high, idx, value)
        self.segTree[segIdx] = max(self.segTree[2*segIdx+1], self.segTree[2*segIdx+2])

    #Util function to update the range
    def __updateRangeUtil(self, segIdx, low, high, l, r, value):      
        #Finish the unprocessed lazy array values
        if self.lazy[segIdx]!=0:
            self.segTree[segIdx] += self.lazy[segIdx] #update value from lazy tree
            #copy the value to the childs of lazy tree
            if low!=high:
                self.lazy[(2*segIdx)+1] = value
                self.lazy[(2*segIdx)+2] = value
            #We are done processing the lazy tree, so make it 0
            self.lazy[segIdx] = 0

        #Lies outside range
        if high<l or low>r:
            return -sys.maxsize
        
        #Lies completely in range
        if low>=l and high<=r :
            #update the value in tree
            self.segTree[segIdx] += value
            #Copy the value to lazy tree for further processing
            if low!=high:
                self.lazy[(2*segIdx)+1] = value
                self.lazy[(2*segIdx)+2] = value
            return

        #partially in range
        mid=(low+high)//2
        self.__updateRangeUtil((2*segIdx)+1, low, mid, l, r, value)
        self.__updateRangeUtil((2*segIdx)+2, mid+1, high, l, r, value)
        self.segTree[segIdx] = max(self.segTree[2*segIdx+1], self.segTree[2*segIdx+2])
    
numOfElements=10
arr = [8,2,5,1,4,5,3,9,6,10]
st = SegmentTree(numOfElements,arr)
print("Input Array: ", arr)
st.buildST()
print("Max is range 5 - 9 : ", end = " ")
print(st.query(5,9))
print("Max is range 1 - 3 : ", end = " ")
print(st.query(1,3)) #Max should be 5
print("Updating the index 1 with +5")
st.updateIdx(1,5) #Update index 1 with +5
#st.printST()
print("Max is range 1 - 3 : ", end = " ")
print(st.query(1,3)) #Now max should be 7 after update
print("Max is range 5 - 6 : ", end = " ")
print(st.query(5,6)) #Max should be 5
print("Updating the range 6 - 7 with +3")
st.updateRange(6,7,3) #Update range 3-4 with +3
print("Max is range 5 - 6 : ", end = " ")
print(st.query(5,6)) #Max should be 5

