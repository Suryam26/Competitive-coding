# Memoization
dp = [-1] * 10


def frogJump(n, height):
    if n == 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    left = frogJump(n-1, height) + abs(height[n] - height[n-1])
    right = float('inf') if n == 1 else frogJump(
        n-2, height) + abs(height[n] - height[n-2])

    dp[n] = min(left, right)
    return dp[n]


# Tabulation
def frogJump2(n, height):
    dp = [-1] * n
    dp[0] = 0

    for i in range(1, n):
        left = dp[i-1] + abs(height[i]-height[i-1])
        right = float(
            'inf') if i == 1 else dp[i-2] + abs(height[i]-height[i-2])
        dp[i] = min(left, right)

    return dp[n-1]


# Optimized Tabulation
def frogJump3(n, height):
    prev2 = 0
    prev = abs(height[0] - height[1])

    for i in range(2, n):
        left = prev + abs(height[i]-height[i-1])
        right = float(
            'inf') if i == 1 else prev2 + abs(height[i]-height[i-2])
        curr = min(left, right)

        prev2, prev = prev, curr

    return curr


h = [10, 20, 30, 10]
print(frogJump(3, h))
print(frogJump2(4, h))
print(frogJump3(4, h))
