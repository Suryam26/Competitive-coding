nums = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(nums)


# Memoization
dp = [[-1 for i in range(n+1)] for j in range(n)]


def lis(i, prev):
    if i == len(nums):
        return 0

    if dp[i][prev+1] != -1:
        return dp[i][prev+1]

    not_take = lis(i+1, prev)
    take = 1 + lis(i+1, i) if prev == - \
        1 or nums[prev] < nums[i] else float('-inf')

    dp[i][prev+1] = max(not_take, take)
    return dp[i][prev+1]


# Tabulation
def lis2(n):
    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    for i in range(n-1, -1, -1):
        for prev in range(i-1, -2, -1):
            not_take = dp[i+1][prev+1]
            take = 1 + dp[i+1][i+1] if prev == - \
                1 or nums[prev] < nums[i] else float('-inf')

            dp[i][prev+1] = max(not_take, take)

    return dp[0][0]


# Optimized Tabulation
def lis3(n):
    next = [0 for i in range(n+1)]

    for i in range(n-1, -1, -1):
        cur = [0 for i in range(n+1)]
        for prev in range(i-1, -2, -1):
            not_take = next[prev+1]
            take = 1 + next[i+1] if prev == - \
                1 or nums[prev] < nums[i] else float('-inf')

            cur[prev+1] = max(not_take, take)

        next = cur

    return next[0]


# Approach - 1
def print_seq(hash, last_index):
    seq = [nums[last_index]]
    while hash[last_index] != last_index:
        last_index = hash[last_index]
        seq.append(nums[last_index])

    return seq[::-1]


def lis4(n):
    next = [1 for i in range(n)]
    hash = [0 for i in range(n)]

    last_index = 0
    maxi = 1
    for i in range(n):
        hash[i] = i
        for prev in range(i):
            if nums[prev] < nums[i] and 1 + next[prev] > next[i]:
                next[i] = 1 + next[prev]
                hash[i] = prev

        if next[i] > maxi:
            maxi = next[i]
            last_index = i

    # print(print_seq(hash, last_index))
    return maxi


# Approach - 2 (Best)
def binary_search(arr, x):
    l, r = 0, len(arr)-1

    flag = False
    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1
            flag = True
        else:
            flag = False
            r = mid - 1

    if flag and mid != len(arr)-1:
        return mid + 1
    return mid


def lis5(n):
    result = [nums[0]]

    for i in range(1, n):
        if nums[i] > result[-1]:
            result.append(nums[i])
        else:
            ind = binary_search(result, nums[i])
            result[ind] = nums[i]

    return len(result)


print(lis(0, -1))
print(lis2(n))
print(lis3(n))
print(lis4(n))
print(lis5(n))
