'''
QUICK SELECT ALGORITHM
Best & Avg Case: O(n)
Worst Case: O(n^2)
'''
def partition(arr, start,end):
    pivotElement = arr[end]
    pivot=start
    for i in range(start,end):
        if arr[i]<=pivotElement:
            arr[i],arr[pivot]=arr[pivot],arr[i]
            pivot+=1
    arr[end],arr[pivot]=arr[pivot],arr[end]
    return pivot


def quickselect(arr, start, end, k):
    pivot = partition(arr,start, end)
    if pivot==k-1:
        return arr[pivot]
    elif pivot<k-1:
        return quickselect(arr, pivot+1, end, k)
    else:
        return quickselect(arr, start, pivot-1, k)
        
arr = [7,2,1,9,3,6,8]
n = len(arr)
k=4
print(f"{k}th smallest element = ", quickselect(arr, 0, n-1, k))
print(arr)
# print("Sorted: ", sorted(arr))
