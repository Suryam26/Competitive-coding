
from itertools import count


def getPairsCount(arr, n, k):
    d = {}
    count = 0
    for i in arr:
        diff = k - i
        if diff in d:
            count += d[diff]

        if i not in d:
            d[i] = 0
        d[i] += 1        
    
    return count

arr = [1, 5, 7, 1]
k = 6
print(getPairsCount(arr, len(arr), k))