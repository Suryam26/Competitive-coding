def calculate_min_platforms(at, dt):
    at.sort()
    dt.sort()

    ans = 1
    count = 1
    i, j = 1, 0
    while i < len(at) and j < len(dt):
        if at[i] <= dt[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        ans = max(ans, count)
    return ans


at = [900, 940, 950, 1100, 1500, 1800]
dt = [910, 1200, 1120, 1130, 1900, 2000]
print(calculate_min_platforms(at, dt))
