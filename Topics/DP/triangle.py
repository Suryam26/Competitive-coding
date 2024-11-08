t = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
n = len(t)


# Memoization
dp = [[-1 for i in range(n)] for j in range(n)]


def triangle(i, j, n):
    if i == n-1:
        dp[i][j] = t[i][j]
        return dp[i][j]

    if dp[i][j] != -1:
        return dp[i][j]

    down = t[i][j] + triangle(i+1, j, n)
    diagonal = t[i][j] + triangle(i+1, j+1, n)

    dp[i][j] = min(down, diagonal)
    return dp[i][j]


# Tabulation
def triangle2(n):
    dp = [[-1 for i in range(n)] for j in range(n)]

    dp[-1] = t[-1]

    for i in range(n-2, -1, -1):
        for j in range(i, -1, -1):
            down = t[i][j] + dp[i+1][j]
            diagonal = t[i][j] + dp[i+1][j+1]

            dp[i][j] = min(down, diagonal)

    return dp[0][0]


# Optimized Tabulation
def triangle3(n):
    prev = t[-1].copy()

    for i in range(n-2, -1, -1):
        temp = [-1] * n
        for j in range(i, -1, -1):
            down = t[i][j] + prev[j]
            diagonal = t[i][j] + prev[j+1]

            temp[j] = min(down, diagonal)

        prev = temp

    return prev[0]


print(triangle(0, 0, n))
print(triangle2(n))
print(triangle3(n))
