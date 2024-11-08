def two_sum(arr, target):
    result = []
    hashmap = {}
    for i in arr:
        val = target - i
        if val in hashmap and hashmap[val] > 0:
            result.append([i, val])
            hashmap[val] -= 1
        else:
            hashmap[i] = hashmap.get(i, 0) + 1

    if len(result):
        return result
    return [[-1, -1]]


a = [2, 7, 11, 13]
print(two_sum(a, 9))
