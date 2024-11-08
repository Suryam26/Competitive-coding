matrix = [
    [1, 1],
    [0, 0],
    [1, 1]
]

n, m = len(matrix), len(matrix[0])


def countSubmatrix(n, m):
    count = [[0 for j in range(m)] for i in range(n)]
    count[0] = matrix[0]
    ans = sum(count[0])

    for i in range(1, n):
        count[i][0] = matrix[i][0]
        ans += count[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j]:
                count[i][j] = 1 + min(count[i-1][j-1],
                                      count[i-1][j], count[i][j-1])
                ans += count[i][j]

    return ans


print(countSubmatrix(n, m))
