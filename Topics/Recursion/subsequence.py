_input = [3, 1, 2]


def subsequence(i, n, arr):
    if i == n:
        print(arr)
        return

    # not picking
    subsequence(i+1, n, arr)

    # picking
    arr.append(_input[i])
    subsequence(i+1, n, arr)
    arr.pop()


subsequence(0, len(_input), [])
