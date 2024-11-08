def nearest(grid):
    """
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    """
    n, m = len(grid), len(grid[0])
    move = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    ans = [[0] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]

    queue = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                visited[i][j] = True
                queue.append((i, j, 0))

    while queue:
        i, j, step = queue.pop(0)
        ans[i][j] = step

        for x, y in move:
            new_i, new_j = i + x, j + y
            if 0 <= new_i < n and 0 <= new_j < m and not visited[new_i][new_j]:
                queue.append((new_i, new_j, step + 1))
                visited[new_i][new_j] = True

    return ans


print(nearest([[1, 0, 1], [1, 1, 0], [1, 0, 0]]))
