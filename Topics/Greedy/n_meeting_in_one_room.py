def maximum_meetings(start, end):
    n = len(start)

    schedule = []
    for i in range(n):
        schedule.append((start[i], end[i]))

    sorted_s = sorted(schedule, key=lambda x: x[1])

    ans = 1
    prev = sorted_s[0]
    for i in range(1, n):
        if sorted_s[i][0] > prev[1]:
            ans += 1
            prev = sorted_s[i]

    return ans


s = [1, 3, 6]
e = [4, 8, 7]

print(maximum_meetings(s, e))
