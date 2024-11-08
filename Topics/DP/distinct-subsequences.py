s = "babgbag"
t = "bag"
n, m = len(s), len(t)

dp = [[-1 for i in range(m)] for j in range(n)]


def distinctSubsequ(n, m):
    if m < 0:
        return 1

    if n < 0:
        return 0

    if dp[n][m] != -1:
        return dp[n][m]

    if s[n] == t[m]:
        dp[n][m] = distinctSubsequ(n-1, m-1) + distinctSubsequ(n-1, m)
        return dp[n][m]
    else:
        dp[n][m] = distinctSubsequ(n-1, m)
        return dp[n][m]


def distinctSubsequ2(n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]

    for j in range(m+1):
        dp[0][j] = 0

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


def distinctSubsequ3(n, m):
    prev = [0 for i in range(m+1)]
    prev[0] = 1

    for i in range(1, n+1):
        for j in range(m, 0, -1):
            if s[i-1] == t[j-1]:
                prev[j] = prev[j-1] + prev[j]

    return prev[-1]


print(distinctSubsequ(n-1, m-1))
print(distinctSubsequ2(n, m))
print(distinctSubsequ3(n, m))
