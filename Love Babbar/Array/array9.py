# Minimise the maximum difference between heights.

def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[-1] - arr[0]
    small = arr[0] + k
    large = arr[-1] - k
    for i in range(n-1):
        mn = min(small, arr[i+1] - k)
        mx = max(large, arr[i] + k)
        if mn < 0: 
            continue
        ans = min(ans, mx - mn)
    return ans

print(getMinDiff([1,5,15,10], 4, 3))