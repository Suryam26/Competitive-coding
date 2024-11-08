grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
]
m, n = len(grid), len(grid[0])


# Memoization
dp = [[-1 for i in range(n)] for j in range(m)]


def minPathSum(m, n):
    if m == 0 and n == 0:
        dp[m][n] = grid[m][n]
        return dp[m][n]

    if m < 0 or n < 0:
        return float('inf')

    if dp[m][n] != -1:
        return dp[m][n]

    up = grid[m][n] + minPathSum(m-1, n)
    left = grid[m][n] + minPathSum(m, n-1)

    dp[m][n] = min(up, left)

    return dp[m][n]


# Tabulation
def minPathSum2(m, n):
    dp = [[-1 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):

            if i == 0 and j == 0:
                dp[i][j] = grid[0][0]
                continue

            up = grid[i][j] + dp[i-1][j] if i > 0 else float('inf')
            left = grid[i][j] + dp[i][j-1] if j > 0 else float('inf')
            dp[i][j] = min(up, left)

    return dp[-1][-1]


# Optimized Tabulation
def minPathSum3(m, n):
    prev_row = [0] * n

    for i in range(m):

        temp = [0] * n
        for j in range(n):

            if i == 0 and j == 0:
                temp[j] = grid[0][0]
                continue

            up = grid[i][j] + prev_row[j] if i > 0 else float('inf')
            left = grid[i][j] + temp[j-1] if j > 0 else float('inf')

            temp[j] = min(up, left)

        prev_row = temp

    return prev_row[-1]


print(minPathSum(m-1, n-1))
print(minPathSum2(m, n))
print(minPathSum3(m, n))
