def dfs(i, j, visited, grid):
    n, m = len(grid), len(grid[0])

    if i < 0 or i >= n or j < 0 or j >= m:
        return

    if grid[i][j] == 0 or (i, j) in visited:
        return

    visited.add((i, j))
    move = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for x, y in move:
        dfs(i + x, j + y, visited, grid)


def num_is_lands(grid):
    """
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    """
    n, m = len(grid), len(grid[0])

    ans = 0
    visited = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and (i, j) not in visited:
                ans += 1
                dfs(i, j, visited, grid)

    return ans


print(num_is_lands([[0, 1], [1, 0], [1, 1], [1, 0]]))
