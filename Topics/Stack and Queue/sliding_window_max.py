from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    queue = deque()
    ans = []

    for i in range(len(nums)):
        if queue and queue[0] == i - k:
            queue.popleft()

        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()

        queue.append(i)

        if i >= k - 1:
            ans.append(nums[queue[0]])

    return ans
