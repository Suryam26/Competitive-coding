"""
Problem Statement: Given a value V, if we want to make a change for V Rs,
and we have an infinite supply of each of the denominations in Indian currency, i.e.,
we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes,
what is the minimum number of coins and/or notes needed to make the change.

Example 1
Input: V = 70
Output: 2
Explanation: We need a 50 Rs note and a 20 Rs note.
"""

arr = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def minimum_coins(v):
    n = len(arr)

    ans = []
    for i in range(n - 1, -1, -1):
        if v == 0:
            break

        if arr[i] > v:
            continue

        for j in range((v // arr[i])):
            ans.append(arr[i])
        v -= (v // arr[i]) * arr[i]

    return ans


print(minimum_coins(121))
