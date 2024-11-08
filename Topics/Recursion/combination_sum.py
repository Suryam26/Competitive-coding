# Link: https://leetcode.com/problems/combination-sum/

_input = [2, 3, 5]


def combination_sum(i, target, arr):
    if len(_input) == i:
        if target == 0:
            print(arr)
        return

    if target >= _input[i]:
        arr.append(_input[i])
        combination_sum(i, target-_input[i], arr)
        arr.pop()

    combination_sum(i+1, target, arr)


combination_sum(0, 8, [])
