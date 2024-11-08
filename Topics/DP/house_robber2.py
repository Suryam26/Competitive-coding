from house_robber import rob_3


def rob(nums):
    if len(nums) == 1:
        return nums[0]

    return max(rob_3(nums[1:]), rob_3(nums[:-1]))
