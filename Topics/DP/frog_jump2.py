# Frog Jump for k-index
# Memoization
dp = [-1] * 10


def frogJump(n, k, height):
    if n == 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    min_jump = float('inf')
    for i in range(1, k+1):
        if n - i >= 0:
            jump = frogJump(n-i, k, height) + abs(height[n] - height[n-i])
            min_jump = min(min_jump, jump)

    dp[n] = min_jump
    return dp[n]


# Tabulation
def frogJump2(n, k, height):
    dp = [-1] * n
    dp[0] = 0

    for i in range(1, n):

        min_jump = float('inf')
        for j in range(1, k+1):
            if i - j >= 0:
                jump = dp[i-j] + abs(height[i]-height[i-j])
                min_jump = min(min_jump, jump)

        dp[i] = min_jump

    return dp[n-1]


h = [10, 20, 30, 10]
print(frogJump(3, 2, h))
print(frogJump2(4, 2, h))
