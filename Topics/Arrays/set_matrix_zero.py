def set_zeros(matrix: list[list[int]]) -> None:
    n, m = len(matrix), len(matrix[0])
    row, col = [-1] * n, [-1] * m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 0
                col[j] = 0

    for j in range(m):
        if col[j] == 0:
            for i in range(n):
                matrix[i][j] = 0

    for i in range(n):
        if row[i] == 0:
            for j in range(m):
                matrix[i][j] = 0


mat = [
    [1, 0],
    [2, 7],
    [3, 0],
    [4, 8]
]
set_zeros(mat)
