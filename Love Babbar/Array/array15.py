# Next Permutation

def nextPermutation(nums):
    piviot, index = 0, 0
    for i in range(len(nums)-1, 0, -1):
        if nums[i] > nums[i-1]:
            piviot = i-1
            index = i
            break
    
    mindiff = nums[index] - nums[piviot]
    swap = index
    for i in range(index, len(nums)):
        if nums[i] > nums[piviot] and nums[i]-nums[piviot] <= mindiff:
            mindiff = nums[i]-nums[piviot]
            swap = i
    
    nums[piviot], nums[swap] = nums[swap], nums[piviot]
    nums[:] = nums[:index] + nums[index:][::-1]
    return nums

print(nextPermutation([1,3,3]))