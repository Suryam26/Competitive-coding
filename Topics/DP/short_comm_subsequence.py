s1 = 'bleed'
s2 = 'blue'
n, m = len(s1), len(s2)


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

    print(printSubsequence(n, m, dp))
    return dp[-1][-1]


def printSubsequence(i, j, dp):
    ans = ''
    while True:
        if i == 0 or j == 0:
            if i == 0:
                while j > 0:
                    ans = s2[j-1] + ans
                    j -= 1

            if j == 0:
                while i > 0:
                    ans = s1[i-1] + ans
                    i -= 1

            break

        if s1[i-1] == s2[j-1]:
            ans = s1[i-1] + ans
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            ans = s1[i-1] + ans
            i -= 1
        else:
            ans = s2[j-1] + ans
            j -= 1

    return ans


print(longestCommonSubsequence2(n, m))
