# Count Inversions

'''
Method 1
Time Complexity: O(N^2)
'''
def inversionCount(arr, n):
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1
    
    return count


'''
Method 2
Time Complexity: O(NLogN)
'''
def Merge(arr, L, R):
    count = 0
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            count += len(L)-i
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return count


def mergeSort(arr):
    count = 0
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        count += mergeSort(L)
        count += mergeSort(R)
        count += Merge(arr, L, R)

    return count

arr = [2, 4, 1, 3, 5]
print(inversionCount(arr, len(arr)))
print(mergeSort(arr))