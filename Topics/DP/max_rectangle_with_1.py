from largest_rectangle_histogram import largestRectangleArea2

matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]


def maximalRectangle(matrix):
    ans = 0
    n = len(matrix[0])
    temp = [0] * n
    for i in range(len(matrix)):
        for j in range(n):
            if matrix[i][j] != '0':
                temp[j] += int(matrix[i][j])
            else:
                temp[j] = 0

        ans = max(ans, largestRectangleArea2(temp))

    return ans


print(maximalRectangle(matrix))
