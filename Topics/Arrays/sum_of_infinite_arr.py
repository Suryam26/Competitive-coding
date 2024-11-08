# Prefix Sum
def sum_in_ranges(arr, n, queries):
    prefix = [0]
    for i in arr:
        prefix.append(prefix[-1] + i)

    res = []
    val = lambda x: (x // n) * prefix[n] + prefix[x % n]
    for left, right in queries:
        ans = val(right) - val(left - 1)
        res.append(ans % 1000000007)

    return res


a = [10]
q = [[1, 1], [7, 7], [3, 5], [1, 2]]
print(*sum_in_ranges(a, len(a), q))
