a = [4, 3, 2, 1]
k = 5


# Memoization
dp = [[-1 for i in range(k+1)] for j in range(len(a))]


def subsetSum(n, k):
    if k == 0:
        return True

    if n == 0:
        return a[0] == k

    if dp[n][k] != -1:
        return dp[n][k]

    not_pick = subsetSum(n-1, k)
    pick = False if k < a[n] else subsetSum(n-1, k - a[n])

    dp[n][k] = pick or not_pick
    return dp[n][k]


# Tabulation
def subsetSum2(n, k):
    dp = [[False for i in range(k+1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = True

    if a[0] <= k:
        dp[0][a[0]] = True

    for i in range(1, n):
        for j in range(1, k+1):
            not_pick = dp[i-1][j]
            pick = False if j < a[i] else dp[i-1][j-a[i]]

            dp[i][j] = pick or not_pick

    return dp[-1][-1]


# Optimized Tabulation
def subsetSum3(n, k):
    prev = [False for i in range(k+1)]
    prev[0] = True

    if a[0] <= k:
        prev[a[0]] = True

    for i in range(1, n):
        temp = [False for i in range(k+1)]
        temp[0] = True
        for j in range(1, k+1):
            not_pick = prev[j]
            pick = False if j < a[i] else prev[j-a[i]]

            temp[j] = pick or not_pick

        prev = temp

    return prev[-1]


print(subsetSum(len(a)-1, k))
print(subsetSum2(len(a), k))
print(subsetSum3(len(a), k))
