# find Largest sum contiguous Subarray 

def sumSubarray(arr):
    total_max = min(arr)
    current_max = 0

    for i in arr:
        current_max += i
        if current_max > total_max: 
                total_max = current_max
        if current_max < 0:
            current_max = 0
            

    return total_max

print(sumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))