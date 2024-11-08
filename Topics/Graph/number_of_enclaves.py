def bfs(i, j, visited, grid):
    n, m = len(grid), len(grid[0])
    move = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    visited[i][j] = True

    ans = 0
    queue = [(i, j)]
    while queue:
        i, j = queue.pop(0)
        ans += 1

        for x, y in move:
            new_i, new_j = i + x, j + y
            if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] and not visited[new_i][new_j]:
                queue.append((new_i, new_j))
                visited[new_i][new_j] = True

    return ans


def number_of_enclaves(grid) -> int:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    """
    n, m = len(grid), len(grid[0])

    total = 0
    for row in grid:
        total += row.count(1)

    visited = [[False] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] and not visited[i][j] and (i in {0, n - 1} or j in {0, m - 1}):
                total -= bfs(i, j, visited, grid)

    return total


print(number_of_enclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
