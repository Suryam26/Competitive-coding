grid = [
    [3, 1, 1],
    [2, 5, 1],
    [1, 5, 5],
    [2, 1, 1]
]
n, m = len(grid), len(grid[0])


# Memoization
dp = [[[-1 for i in range(m)] for i in range(m)] for j in range(n)]


def cherryPick(n, x, y):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid[0]):
        return float('-inf')

    if n == len(grid)-1:
        if x == y:
            dp[n][x][y] = float('-inf')
        else:
            dp[n][x][y] = grid[n][x] + grid[n][y]
        return dp[n][x][y]

    if dp[n][x][y] != -1:
        return dp[n][x][y]

    maxCherry = float('-inf')
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if x != y:
                cherry = grid[n][x] + grid[n][y] + cherryPick(n+1, x+i, y+j)
                maxCherry = max(maxCherry, cherry)

    dp[n][x][y] = maxCherry
    return dp[n][x][y]


# Tabulation
def cherryPick2(n, m):
    dp = [[[-1 for i in range(m)] for i in range(m)] for j in range(n)]

    for i in range(m):
        for j in range(m):
            if i != j:
                dp[n-1][i][j] = grid[n-1][i] + grid[n-1][j]

    for row in range(n-2, -1, -1):
        for x in range(m):
            for y in range(m):

                maxCherry = float('-inf')
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if x != y:
                            cherry = grid[row][x] + grid[row][y]
                            if x+i < 0 or y+j < 0 or x+i >= len(grid[0]) or y+j >= len(grid[0]):
                                cherry = float('-inf')
                                continue
                            else:
                                cherry += dp[row+1][x+i][y+j]
                            maxCherry = max(maxCherry, cherry)

                dp[row][x][y] = maxCherry

    return dp[0][0][m-1]


# Optimized Tabulation
def cherryPick3(n, m):
    prev = [[-1 for i in range(m)] for i in range(m)]

    for i in range(m):
        for j in range(m):
            if i != j:
                prev[i][j] = grid[n-1][i] + grid[n-1][j]

    for row in range(n-2, -1, -1):
        temp = [[-1 for i in range(m)] for i in range(m)]
        for x in range(m):
            for y in range(m):

                maxCherry = float('-inf')
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if x != y:
                            cherry = grid[row][x] + grid[row][y]
                            if x+i < 0 or y+j < 0 or x+i >= len(grid[0]) or y+j >= len(grid[0]):
                                cherry = float('-inf')
                                continue
                            else:
                                cherry += prev[x+i][y+j]
                            maxCherry = max(maxCherry, cherry)

                temp[x][y] = maxCherry

        prev = temp

    return prev[0][m-1]


print(cherryPick(0, 0, m-1))
print(cherryPick2(n, m))
print(cherryPick3(n, m))
