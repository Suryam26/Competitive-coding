# Link: https://practice.geeksforgeeks.org/problems/subset-sums2234/1#

_input = [2, 3]


def subset_sum(i, arr, _sum):
    if i == len(_input):
        print(_sum, end=" ")
        return

    subset_sum(i+1, arr, _sum)

    arr.append(_input[i])
    subset_sum(i+1, arr, _sum+_input[i])
    arr.pop()


subset_sum(0, [], 0)
