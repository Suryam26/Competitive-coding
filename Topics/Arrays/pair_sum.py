# Two Sum
def pair_sum(arr, s):
    hashmap = {}
    res = []
    for i in arr:
        val = s - i
        if val in hashmap:
            for _ in range(hashmap[val]):
                l = min(i, val)
                r = max(i, val)
                res.append([l, r])
        hashmap[i] = hashmap.get(i, 0) + 1

    return sorted(res, key=lambda x: x[0])


print(pair_sum([1, 2, 3, 4, 5], 5))
