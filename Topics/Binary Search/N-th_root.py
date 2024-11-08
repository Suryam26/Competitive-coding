"""
Problem Statement: https://www.codingninjas.com/studio/problems/1062679
Explanation: https://takeuforward.org/data-structure/nth-root-of-a-number-using-binary-search/
"""


# Brute Force Approach
def find_nth_root_of_m(n, m):
    low, high = 1, m

    for i in range(low, high+1):
        if i ** n == m:
            return i
        elif i ** n > m:
            return -1

    return -1


# Binary Search Approach
def find_nth_root_of_m2(n, m):
    low, high = 1, m

    while low <= high:
        mid = int((high + low) / 2)

        if mid ** n == m:
            return mid
        elif mid ** n < m:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(find_nth_root_of_m2(3, 27))
