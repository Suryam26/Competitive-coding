weight = [1, 2, 4, 5]
val = [5, 4, 8, 6]
n, w = len(val), 5


# Memoization
dp = [[-1 for i in range(w+1)] for j in range(n)]


def knapsack(n, w):
    if dp[n][w] != -1:
        return dp[n][w]

    if n == 0:
        if weight[0] <= w:
            dp[0][w] = val[0]
        else:
            dp[0][w] = 0
        return dp[0][w]

    pick = float('-inf') if weight[n] > w else val[n] + \
        knapsack(n-1, w - weight[n])
    not_pick = knapsack(n-1, w)

    dp[n][w] = max(pick, not_pick)
    return dp[n][w]


# Tabulation
def knapsack2(n, w):
    dp = [[-1 for i in range(w+1)] for j in range(n)]

    for i in range(w+1):
        if weight[0] <= i:
            dp[0][i] = val[0]
        else:
            dp[0][i] = 0

    for i in range(1, n):
        for j in range(w+1):
            pick = float(
                '-inf') if weight[i] > j else val[i] + dp[i-1][j - weight[i]]
            not_pick = dp[i-1][j]

            dp[i][j] = max(pick, not_pick)

    return dp[-1][-1]


# Optimized Tabulation
def knapsack3(n, w):
    prev = [-1 for i in range(w+1)]

    for i in range(w+1):
        if weight[0] <= i:
            prev[i] = val[0]
        else:
            prev[i] = 0

    for i in range(1, n):
        for j in range(w, -1, -1):
            pick = float(
                '-inf') if weight[i] > j else val[i] + prev[j - weight[i]]
            not_pick = prev[j]

            prev[j] = max(pick, not_pick)


    return prev[-1]


print(knapsack(n-1, w))
print(knapsack2(n, w))
print(knapsack3(n, w))
