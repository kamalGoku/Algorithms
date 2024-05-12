'''
Returns the first index which is greater than the key
'''
def upperBound(arr: [int], x: int, n: int) -> int:
    start=0
    end=n-1
    ub=n
    while start<=end:
        mid = (start+end)//2
        if arr[mid]<=x:
            start=mid+1
        else:
            ub = mid
            end = mid-1
    return ub
