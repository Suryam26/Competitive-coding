def next_greater_elements(nums: list[int]) -> list[int]:
    nums += nums
    n = len(nums)

    stack, ans = [], [-1] * n

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]

        stack.append(nums[i])

    return ans[:n//2]


print(next_greater_elements([1, 3, 4, 2]))
