def single_non_duplicate(nums: list[int]) -> int:
    n = len(nums)
    low, high = 0, n - 2

    while low <= high:
        mid = (low + high) // 2

        if mid % 2 == 0:
            if nums[mid] == nums[mid+1]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[mid] == nums[mid+1]:
                high = mid - 1
            else:
                low = mid + 1

    return nums[low]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(single_non_duplicate(nums))
