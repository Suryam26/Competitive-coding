m, n = 3, 7

# Memoization
dp = [[-1 for i in range(n)] for j in range(m)]


def totalUnique(m, n):
    if dp[m][n] != -1:
        return dp[m][n]

    if m == 0 and n == 0:
        dp[m][n] = 1
        return dp[m][n]

    if m < 0 or n < 0:
        return 0

    up = totalUnique(m-1, n)
    left = totalUnique(m, n-1)

    dp[m][n] = up + left

    return dp[m][n]


# Tabulation
def totalUnique2(m, n):
    dp = [[-1 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):

            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            up = dp[i-1][j] if i > 0 else 0
            left = dp[i][j-1] if j > 0 else 0
            dp[i][j] = up + left

    return dp[-1][-1]


# Optimized Tabulation
def totalUnique3(m, n):
    prev_row = [0] * n

    for i in range(m):

        temp = [0] * n
        for j in range(n):

            if i == 0 and j == 0:
                temp[j] = 1
                continue

            up = prev_row[j] if i > 0 else 0
            left = temp[j-1] if j > 0 else 0

            temp[j] = up + left

        prev_row = temp

    return prev_row[-1]


# Combination
def totalUnique4(m, n):
    N = m + n - 2
    r = m - 1
    result = 1

    for i in range(1, r+1):
        result = result * (N - r + i) / i

    return int(result)


print(totalUnique(m-1, n-1))
print(totalUnique2(m, n))
print(totalUnique3(m, n))
print(totalUnique4(m, n))
