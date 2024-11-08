# Link: https://leetcode.com/problems/subsets-ii/

_input = [1, 2, 2]
_input.sort()


def subset_sum(i, arr):
    print(arr)
    for j in range(i, len(_input)):
        if j > i and _input[j] == _input[j-1]:
            continue

        arr.append(_input[j])
        subset_sum(j+1, arr)
        arr.pop()


subset_sum(0, [])
