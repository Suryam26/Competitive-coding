a = [4, 5, 3, 2]
n = len(a)


dp = [[-1 for i in range(n)] for j in range(n)]


def mcm(i, j):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    result = float('inf')
    for k in range(i, j):
        steps = a[i-1] * a[k] * a[j]
        steps += mcm(i, k) + mcm(k+1, j)
        result = min(result, steps)

    dp[i][j] = result
    return dp[i][j]


def mcm2(n):
    dp = [[-1 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for i in range(n-1, 0, -1):
        for j in range(i+1, n):
            result = float('inf')
            for k in range(i, j):
                steps = a[i-1] * a[k] * a[j]
                steps += dp[i][k] + dp[k+1][j]
                result = min(result, steps)
                dp[i][j] = result

    return dp[1][-1]


print(mcm(1, n-1))
print(mcm2(n))


# def mcm3(n):
#     next = [-1 for i in range(n)]
#     next[0] = 0

#     for i in range(n-1, -1, -1):
#         for j in range(i, n):

#             cur = [-1 for i in range(n)]
#             if i == j: cur[i] = 0

#             result = float('inf')
#             for k in range(i, j):
#                 steps = a[i-1] * a[k] * a[j]
#                 steps += dp[i][k] + dp[k+1][j]
#                 result = min(result, steps)
#                 cur[j] = result

#     return dp[1][-1]
