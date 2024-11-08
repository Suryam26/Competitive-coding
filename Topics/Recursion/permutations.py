# Link: https://leetcode.com/problems/permutations/

_input = [1, 2, 3]


# Approach 1:
def permutations(arr, map):
    if len(arr) == len(_input):
        print(arr)
        return

    for i in range(len(_input)):
        if not map[i]:
            map[i] = True
            arr.append(_input[i])
            permutations(arr, map)
            arr.pop()
            map[i] = False


m = [False] * len(_input)
permutations([], m)


# Approach 2:
def permutations2(i):
    if i == len(_input):
        print(_input)
        return

    for j in range(i, len(_input)):
        _input[i], _input[j] = _input[j], _input[i]
        permutations2(i + 1)
        _input[i], _input[j] = _input[j], _input[i]


permutations2(0)


def permutations3(nums):
    n = len(nums)

    ans, curr = [], []

    def sol(i):
        if i == n:
            ans.append(curr[:])

        for j in nums:
            if j not in curr:
                curr.append(j)
                sol(i + 1)
                curr.pop()

    sol(0)
    return ans
