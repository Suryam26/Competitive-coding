'''
Given an array which consists of only 0, 1 and 2. 
Sort the array without using any sorting algo
'''

def sorting(arr):
    freq = {0: 0, 1: 0, 2: 0}
    for i in arr:
        freq[i] += 1
    
    result = []
    for i in range(0, 3):
        for j in range(0, freq[i]):
            result.append(i)

    return result


print(sorting([0,2,1,0,1,2]))