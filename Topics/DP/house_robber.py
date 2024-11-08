nums = [1, 2, 3, 1]

# Memoization
dp = [-1] * len(nums)


def rob(n, nums):
    if n < 0:
        return 0
    if n == 0:
        return nums[0]

    if dp[n] != -1:
        return dp[n]

    pick = nums[n] + rob(n-2, nums)
    not_pick = rob(n-1, nums)

    dp[n] = max(pick, not_pick)
    return dp[n]


# Tabulation
def rob_2(nums):
    dp = [-1] * len(nums)
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        pick = nums[i] if i-2 < 0 else nums[i] + dp[i-2]
        not_pick = dp[i-1]
        dp[i] = max(pick, not_pick)

    return dp[-1]


# Optimized Tabulation
def rob_3(nums):
    prev2 = 0
    prev = nums[0] 

    for i in range(1, len(nums)):
        pick = nums[i] + prev2
        not_pick = prev
        curr = max(pick, not_pick)

        prev2, prev = prev, curr

    return curr


print(rob(len(nums)-1, nums))
print(rob_2(nums))
print(rob_3(nums))
