nums = [3, 1, 5, 8]
nums.insert(0, 1)
nums.append(1)
n = len(nums)


dp = [[-1 for i in range(n-1)] for j in range(n)]


def burst_balloons(i, j):
    if i > j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    maxi = float('-inf')
    for k in range(i, j+1):
        cost = nums[i-1] * nums[k] * nums[j+1] + \
               burst_balloons(i, k - 1) + burst_balloons(k + 1, j)
        maxi = max(maxi, cost)

    dp[i][j] = maxi
    return dp[i][j]


def burst_balloons2(n):
    dp = [[0 for i in range(n-1)] for j in range(n)]

    for i in range(n-2, 0, -1):
        for j in range(i, n-1):
            maxi = float('-inf')
            for k in range(i, j+1):
                cost = nums[i-1]*nums[k]*nums[j+1] + \
                    dp[i][k-1] + dp[k+1][j]
                maxi = max(maxi, cost)

            dp[i][j] = maxi

    return dp[1][-1]


print(burst_balloons(1, n - 2))
print(burst_balloons2(n))
