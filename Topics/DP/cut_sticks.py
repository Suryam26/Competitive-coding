n = 7
cuts = [1, 3, 4, 5]
cuts.append(0)
cuts.append(n)
cuts.sort()
x = len(cuts)


dp = [[-1 for i in range(x-1)] for j in range(x)]


def cutSticks(i, j):
    if i > j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    mini = float('inf')
    for k in range(i, j+1):
        cost = cuts[j+1] - cuts[i-1] + cutSticks(i, k-1) + cutSticks(k+1, j)
        mini = min(cost, mini)

    dp[i][j] = mini
    return dp[i][j]


def cutSticks2(x):
    dp = [[0 for i in range(x-1)] for j in range(x)]

    for i in range(x-2, 0, -1):
        for j in range(i, x-1):
            mini = float('inf')
            for k in range(i, j+1):
                cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
                mini = min(cost, mini)

            dp[i][j] = mini

    return dp[1][-1]


print(cutSticks(1, x-2))
print(cutSticks2(x))
