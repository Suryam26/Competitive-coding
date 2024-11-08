s1 = 'abcjklp'
s2 = 'acjkp'
n, m = len(s1), len(s2)


# Tabulation
def longestCommonString(n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(m+1):
        dp[0][i] = 0

    for j in range(n+1):
        dp[j][0] = 0

    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0

    return ans


# Optimized Tabulation
def longestCommonString2(n, m):
    prev = [0 for i in range(m+1)]

    ans = 0
    for i in range(1, n+1):
        temp = [-1 for i in range(m+1)]
        temp[0] = 0
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                temp[j] = 1 + prev[j-1]
                ans = max(ans, temp[j])
            else:
                temp[j] = 0

        prev = temp

    return ans


print(longestCommonString(n, m))
print(longestCommonString2(n, m))
