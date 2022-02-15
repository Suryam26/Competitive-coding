# Write a program to cyclically rotate an array by one.

def rotate(arr):
    arr.insert(0, arr.pop())
    return arr

print(rotate([1,2,3,4,5]))