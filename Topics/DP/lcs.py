s1 = 'bleed'
s2 = 'blue'
n, m = len(s1), len(s2)


# Memoization
dp = [[-1 for i in range(m)] for j in range(n)]


def longestCommonSubsequence(n, m):
    if n < 0 or m < 0:
        return 0

    if dp[n][m] != -1:
        return dp[n][m]

    if s1[n] == s2[m]:
        dp[n][m] = 1 + longestCommonSubsequence(n-1, m-1)
        return dp[n][m]

    dp[n][m] = max(longestCommonSubsequence(n, m-1),
                   longestCommonSubsequence(n-1, m))
    return dp[n][m]


# Tabulation
def longestCommonSubsequence2(n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(m+1):
        dp[0][i] = 0

    for j in range(n+1):
        dp[j][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    # print(printSubsequence(n, m, dp))
    return dp[-1][-1]


# Optimized Tabulation
def longestCommonSubsequence3(n, m):
    prev = [0 for i in range(m+1)]

    for i in range(1, n+1):
        temp = [-1 for i in range(m+1)]
        temp[0] = 0
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                temp[j] = 1 + prev[j-1]
            else:
                temp[j] = max(temp[j-1], prev[j])

        prev = temp

    return prev[-1]


# Print the subsequence
def printSubsequence(i, j, dp):
    ans = ''
    while True:
        if i == 0 or j == 0:
            break

        if s1[i-1] == s2[j-1]:
            ans = s1[i-1] + ans
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ans


print(longestCommonSubsequence(n-1, m-1))
print(longestCommonSubsequence2(n, m))
print(longestCommonSubsequence3(n, m))
