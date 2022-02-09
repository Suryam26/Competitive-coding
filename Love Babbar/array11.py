# Find duplicate in an array of N+1 Integers

def findDuplicate(nums):
    a = {}
    for i in nums:
        if i in a:
            return i
        else:
            a[i] = 1