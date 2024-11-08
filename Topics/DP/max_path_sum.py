arr = [
    [10, 2, 3],
    [3, 7, 2],
    [8, 1, 5]
]

n, m = len(arr), len(arr[0])


# Memoization
dp = [[-1 for i in range(m)] for j in range(n)]


def maxPath(i, j):
    if j < 0 or j >= len(arr[0]):
        return float('-inf')

    if i == 0:
        dp[i][j] = arr[0][j]
        return dp[i][j]

    if dp[i][j] != -1:
        return dp[i][j]

    up = arr[i][j] + maxPath(i-1, j)
    left_dia = arr[i][j] + maxPath(i-1, j-1)
    right_dia = arr[i][j] + maxPath(i-1, j+1)

    dp[i][j] = max(up, left_dia, right_dia)
    return dp[i][j]


max_path = float('-inf')
for j in range(m):
    max_path = max(max_path, maxPath(n-1, j))


# Tabulation
def maxPath2(n, m):
    dp = [[-1 for i in range(m)] for j in range(n)]

    dp[0] = arr[0].copy()

    for i in range(1, n):
        for j in range(0, m):
            up = arr[i][j] + dp[i-1][j]
            left_dia = float('-inf') if j == 0 else arr[i][j] + dp[i-1][j-1]
            right_dia = float('-inf') if j == m-1 else arr[i][j] + dp[i-1][j+1]

            dp[i][j] = max(up, left_dia, right_dia)

    return max(dp[-1])


# Optimized Tabulation
def maxPath3(n, m):
    prev = arr[0].copy()

    for i in range(1, n):
        temp = [-1 for i in range(m)]
        for j in range(0, m):
            up = arr[i][j] + prev[j]
            left_dia = float('-inf') if j == 0 else arr[i][j] + prev[j-1]
            right_dia = float('-inf') if j == m-1 else arr[i][j] + prev[j+1]

            temp[j] = max(up, left_dia, right_dia)

        prev = temp

    return max(prev)


print(max_path)
print(maxPath2(n, m))
print(maxPath3(n, m))
