# Reverse the array

def reverse(arr):
    i, j = 0, len(arr)-1
    while j >= i:
        arr[i], arr[j] = arr[j], arr[i] 
        i += 1
        j -= 1
    
    return arr

print(reverse([1,2,3,4,5,6,7]))