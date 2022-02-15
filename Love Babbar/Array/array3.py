# Find the "Kth" max and min element of an array 

def maxmin(arr, n):
    arr.sort()
    print("MIN:", arr[n-1])
    print("MAX:", arr[-n])

maxmin([2,1,4,5,3,6,7], 3)