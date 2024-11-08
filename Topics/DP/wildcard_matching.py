s = "aa"
p = "*"
n, m = len(p), len(s)


dp = [[False for i in range(m)] for j in range(n)]


def wildcardMatching(n, m):
    if m < 0 and n < 0:
        return True

    if n < 0 and m >= 0:
        return False

    if m < 0 and n >= 0:
        for i in range(n+1):
            if p[i] != '*':
                return False
        return True

    if dp[n][m] != False:
        return dp[n][m]

    if p[n] == s[m] or p[n] == '?':
        dp[n][m] = wildcardMatching(n-1, m-1)
        return dp[n][m]

    if p[n] == '*':
        empty = wildcardMatching(n-1, m)
        non_empty = wildcardMatching(n, m-1)
        dp[n][m] = empty or non_empty
        return dp[n][m]

    dp[n][m] = False
    return dp[n][m]


def wildcardMatching2(n, m):
    dp = [[False for i in range(m+1)] for j in range(n+1)]

    dp[0][0] = True

    for j in range(1, m+1):
        dp[0][j] = False

    for i in range(1, n+1):
        dp[i][0] = True
        for k in range(i):
            if p[k] != '*':
                dp[i][0] = False
                break

    for i in range(1, n+1):
        for j in range(1, m+1):
            if p[i-1] == s[j-1] or p[i-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif p[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j] = False

    return dp[-1][-1]


def wildcardMatching3(n, m):
    prev = [False for i in range(m+1)]
    prev[0] = True

    for i in range(1, n+1):
        temp = [False for i in range(m+1)]
        temp[0] = True

        for k in range(i):
            if p[k] != '*':
                temp[0] = False
                break

        for j in range(1, m+1):
            if p[i-1] == s[j-1] or p[i-1] == '?':
                temp[j] = prev[j-1]
            elif p[i-1] == '*':
                temp[j] = prev[j] or temp[j-1]
            else:
                temp[j] = False

        prev = temp

    return prev[-1]


print(wildcardMatching(n-1, m-1))
print(wildcardMatching2(n, m))
print(wildcardMatching3(n, m))
