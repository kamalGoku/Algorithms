'''
Returns the first index after the key
'''
def lowerBound(arr: [int], n: int, x: int) -> int:
    start = 0
    end = n-1
    lb=n
    while start<=end:
        mid = (start+end)//2
        if arr[mid]>=x:
            lb = mid
            end=mid-1
        else:
            start = mid+1
    return lb
