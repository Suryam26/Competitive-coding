points = [
    [18, 11, 19],
    [4, 13, 7],
    [1, 8, 13],
]


# Memoization
dp = [[-1 for i in range(4)] for j in range(len(points))]


def ninja(day, last, points):
    if dp[day][last] != -1:
        return dp[day][last]

    if day == 0:
        maxi = 0
        for i in range(0, 3):
            if i != last:
                maxi = max(maxi, points[0][i])

        dp[day][last] = maxi
        return dp[day][last]

    maxi = 0
    for i in range(0, 3):
        if i != last:
            point = points[day][i] + ninja(day-1, i, points)
            maxi = max(maxi, point)

    dp[day][last] = maxi
    return dp[day][last]


# Tabulation
def ninja2(points):
    dp = [[-1 for i in range(4)] for j in range(len(points))]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0])

    for day in range(1, len(points)):
        for last in range(4):
            for i in range(3):
                if i != last:
                    point = points[day][i] + dp[day-1][i]
                    dp[day][last] = max(dp[day][last], point)

    return dp[len(points)-1][3]


# Optimized Tabulation
def ninja3(points):
    prev = [-1, -1, -1, -1]

    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0])

    for day in range(1, len(points)):
        temp = [-1, -1, -1, -1]
        for last in range(4):
            for i in range(3):
                if i != last:
                    point = points[day][i] + prev[i]
                    temp[last] = max(temp[last], point)

        prev = temp

    return temp[3]


print(ninja(len(points)-1, 3, points))
print(ninja2(points))
print(ninja3(points))
