# Minimum no. of Jumps to reach end of an array

def minJump(arr, n):
    count = 0
    end = 0
    maxR = 0
    for i in range(n-1):
        maxR = max(maxR, i+arr[i])

        if(i == end):
            count += 1
            end = maxR
        if(arr[i] == 0 and i == end):
            return -1   

    return count

arr = [1, 4, 3, 2, 6, 7]
print(minJump(arr, len(arr)))
