grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
m, n = len(grid), len(grid[0])

# Memoization
dp = [[-1 for i in range(n)] for j in range(m)]


def totalUnique(m, n):
    if m == 0 and n == 0:
        dp[m][n] = 1
        return dp[m][n]

    if m < 0 or n < 0:
        return 0

    if grid[m][n] == 1:
        return 0

    if dp[m][n] != -1:
        return dp[m][n]

    up = totalUnique(m-1, n)
    left = totalUnique(m, n-1)

    dp[m][n] = up + left

    return dp[m][n]


# Tabulation
def totalUnique2(m, n):
    dp = [[-1 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):

            if grid[i][j] == 1:
                dp[i][j] = 0
            else:

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
            
            if grid[i][j] == 1:
                temp[j] = 0
            else:
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue
                
                up = prev_row[j] if i > 0 else 0
                left = temp[j-1] if j > 0 else 0

                temp[j] = up + left

        prev_row = temp

    return prev_row[-1]


print(totalUnique(m-1, n-1))
print(totalUnique2(m, n))
print(totalUnique3(m, n))
