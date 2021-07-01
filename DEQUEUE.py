'''
Problem Code: DEQUEUE
https://www.codechef.com/START4C/problems/DEQUEUE 
'''


def minPop(n, m, arr):
    arr1 = arr[::-1]
    index_count = {}
    prefix = set()
    suffix = set()

    for i in range(1, n+1):
        index_count[i] = arr1.index(i) + 1
        suffix.add(arr1.index(i) + 1)

    minimum = 1000000
    if max(suffix) < minimum:
        minimum = max(suffix)

    for i in range(m):
        if len(suffix) == 0:
            break
        else:
            if arr[i] not in prefix:
                prefix.add(arr[i])
                index = index_count[arr[i]]
                suffix.remove(index)

            if len(suffix) == 0:
                pops = i + 1
            else:
                pops = max(suffix) + i + 1

            if pops < minimum:
                minimum = pops

    return minimum


for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(minPop(n, m, arr))
