#Keep maxSofar and maxHere
#Update maxHere for every element and update the max in maxSoFar
#if maxHere goes <0 then make it 0

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        maxSoFar = -sys.maxsize
        maxHere = 0
        for num in arr:
            maxHere+=num
            if maxSoFar<maxHere:
                maxSoFar = maxHere
            if maxHere<0: maxHere=0
        return maxSoFar
