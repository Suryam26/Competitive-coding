# Merge 2 sorted arrays without using Extra space.

def merge(arr1, arr2, n, m): 
    l1, s2 = n-1, 0
    while arr1[l1] > arr2[s2]:
        arr1[l1], arr2[s2] = arr2[s2], arr1[l1]
        l1 -= 1
        s2 += 1
        if l1 < 0 or s2 == m:
            break
        
    arr1.sort()
    arr2.sort()
    print(*arr1, *arr2)

a1 = [1, 3, 5, 7]
a2 = [0, 2, 6, 8, 9]
merge(a1, a2, len(a1), len(a2))