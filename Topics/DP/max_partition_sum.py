arr = [1, 15, 7, 9, 2, 5, 10]
k = 3
n = len(arr)


dp = [-1 for i in range(n)]


def maxPartition(i, n, k):
    if i == n:
        return 0

    if dp[i] != -1:
        return dp[i]

    ans = float('-inf')
    maxi, l = float('-inf'), 0
    for j in range(i, min(n, i+k)):
        l += 1
        maxi = max(maxi, arr[j])
        sum = l * maxi + maxPartition(j+1, n, k)
        ans = max(ans, sum)

    dp[i] = ans
    return dp[i]


def maxPartition2(n, k):
    dp = [0 for i in range(n+1)]
    dp[n] = 0

    for i in range(n-1, -1, -1):
        ans = float('-inf')
        maxi, l = float('-inf'), 0
        for j in range(i, min(n, i+k)):
            l += 1
            maxi = max(maxi, arr[j])
            sum = l * maxi + dp[j+1]
            ans = max(ans, sum)
            dp[i] = ans

    return dp[0]


print(maxPartition(0, n, k))
print(maxPartition2(n, k))
