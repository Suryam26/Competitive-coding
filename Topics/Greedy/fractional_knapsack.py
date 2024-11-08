def maximum_value(items, w):
    items.sort(key=lambda x: -(x[1] / x[0]))

    ans = 0
    for weight, v in items:
        if w - weight < 0:
            ans += (v / weight) * w
            break
        else:
            ans += v
            w -= weight

    return ans


w = 50
items = [[20, 100], [10, 60], [30, 120]]
print(maximum_value(items, w))
