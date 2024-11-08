# Link: https://leetcode.com/problems/combination-sum-ii/

_input = [2, 5, 2, 1, 2]
_input.sort()


def com_sum(i, target, arr):
    if target == 0:
        print(arr)
        return

    for j in range(i, len(_input)):
        if j > i and _input[j] == _input[j-1]:
            continue
        if _input[j] > target:
            break

        arr.append(_input[j])
        com_sum(j+1, target-_input[j], arr)
        arr.pop()


com_sum(0, 5, [])
