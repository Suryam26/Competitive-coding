# Rearrange the array in alternating positive and 
# negative items with O(1) extra space.

def rearrange(arr):
    pointer = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1

    i = 1
    j = pointer
    while i < len(arr) and j < len(arr) and arr[i] < 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 2
        j += 1

    return arr
    

print(rearrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))