"""
Problem statement: https://www.interviewbit.com/problems/noble-integer/
"""


def solve(A):
    count = {}
    for i in A:
        if i not in count:
            count[i] = 0
        count[i] += 1

    sorted_key = sorted(count.keys())

    n = len(sorted_key)
    left_sum = [0] * len(sorted_key)

    for i in range(n - 2, -1, -1):
        left_sum[i] = count[sorted_key[i + 1]] + left_sum[i + 1]

    for i in range(n):
        if sorted_key[i] == left_sum[i]:
            return 1

    return -1


A = [-4, -2, 0, -1, -6]
print(solve(A))
