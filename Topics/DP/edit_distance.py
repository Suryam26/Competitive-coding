word1 = "intention"
word2 = "execution"
n, m = len(word1), len(word2)


dp = [[-1 for i in range(m)] for j in range(n)]


def editDistance(n, m):
    if n < 0:
        dp[n][m] = m+1
        return m+1

    if m < 0:
        dp[n][m] = n+1
        return n+1

    if dp[n][m] != -1:
        return dp[n][m]

    if word1[n] == word2[m]:
        dp[n][m] = editDistance(n-1, m-1)
        return dp[n][m]
    else:
        inster = 1 + editDistance(n, m-1)
        delete = 1 + editDistance(n-1, m)
        replace = 1 + editDistance(n-1, m-1)
        dp[n][m] = min(inster, delete, replace)
        return dp[n][m]


def editDistance2(n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]

    for j in range(m+1):
        dp[0][j] = j

    for i in range(n+1):
        dp[i][0] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                inster = 1 + dp[i][j-1]
                delete = 1 + dp[i-1][j]
                replace = 1 + dp[i-1][j-1]
                dp[i][j] = min(inster, delete, replace)

    return dp[-1][-1]


def editDistance3(n, m):
    prev = [-1 for i in range(m+1)]

    for j in range(m+1):
        prev[j] = j

    for i in range(1, n+1):
        temp = [-1 for i in range(m+1)]
        temp[0] = i
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                temp[j] = prev[j-1]
            else:
                inster = 1 + temp[j-1]
                delete = 1 + prev[j]
                replace = 1 + prev[j-1]
                temp[j] = min(inster, delete, replace)

        prev = temp

    return prev[-1]


print(editDistance(n-1, m-1))
print(editDistance2(n, m))
print(editDistance3(n, m))
