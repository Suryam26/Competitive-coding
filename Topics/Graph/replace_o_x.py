def dfs(i, j, visited, mat, ans):
    n, m = len(mat), len(mat[0])
    move = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    visited[i][j] = True
    ans[i][j] = 'O'

    for x, y in move:
        new_i, new_j = i + x, j + y
        if 0 <= new_i < n and 0 <= new_j < m and not visited[new_i][new_j] and mat[new_i][new_j] == 'O':
            dfs(new_i, new_j, visited, mat, ans)


def fill(mat):
    """
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    """
    n, m = len(mat), len(mat[0])

    ans = [['X'] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 'O' and not visited[i][j] and (i in {0, n - 1} or j in {0, m - 1}):
                dfs(i, j, visited, mat, ans)

    return ans


print(fill([['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'O', 'X', 'X'],
            ['X', 'X', 'O', 'O']]))
