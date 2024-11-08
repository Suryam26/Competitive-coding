coins = [1, 2, 5]
n, t = len(coins), 11


# Memoization
dp = [[-1 for i in range(t+1)] for j in range(n)]


def min_coins(n, t):
    if n == 0:
        if t % coins[0] == 0:
            dp[n][t] = t//coins[0]
            return dp[n][t]
        return float('inf')

    if dp[n][t] != -1:
        return dp[n][t]

    pick = float('inf') if coins[n] > t else 1 + \
        min_coins(n, t - coins[n])
    not_pick = min_coins(n-1, t)

    dp[n][t] = min(pick, not_pick)
    return dp[n][t]


# Tabulation
def min_coins2(n, t):
    dp = [[-1 for i in range(t+1)] for j in range(n)]

    for i in range(t+1):
        if i % coins[0] == 0:
            dp[0][i] = i//coins[0]
        else:
            dp[0][i] = float('inf')

    for i in range(1, n):
        for j in range(t+1):
            pick = float('inf') if coins[i] > j else 1 + dp[i][j - coins[i]]
            not_pick = dp[i-1][j]

            dp[i][j] = min(pick, not_pick)

    return dp[-1][-1]


# # Optimized Tabulation
def min_coins3(n, t):
    prev = [-1 for i in range(t+1)]

    for i in range(t+1):
        if i % coins[0] == 0:
            prev[i] = i//coins[0]
        else:
            prev[i] = float('inf')

    for i in range(1, n):
        temp = [-1 for i in range(t+1)]
        for j in range(t+1):
            pick = float('inf') if coins[i] > j else 1 + temp[j - coins[i]]
            not_pick = prev[j]

            temp[j] = min(pick, not_pick)

        prev = temp

    return prev[-1]


print(min_coins(n-1, t))
print(min_coins2(n, t))
print(min_coins3(n, t))
