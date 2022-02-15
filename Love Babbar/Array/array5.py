# Move all the negative elements to one side of the array.

def move(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr

print (move([-12, 11, -13, -5, 6, -7, 5, -3, -6]))