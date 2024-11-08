"""
Problem Statement: https://www.interviewbit.com/problems/minimum-lights-to-activate/
"""


def solve(A, B):
    n = len(A)
    ans = 0

    i = 0
    while i < n:
        left = max(0, i - B + 1)
        right = min(i + B - 1, n - 1)

        found = False
        while right > left:
            if A[right] == 1:
                found = True
                break
            right -= 1

        if not found:
            return -1

        ans += 1
        i = right + B

    return ans


A = [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0]
B = 12
print(solve(A, B))
