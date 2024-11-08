move = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def dfs(i, j, visited, grid):
    n, m = len(grid), len(grid[0])

    visited.add((i, j))

    ans = []
    for x, y in move:
        new_i, new_j = i + x, j + y

        if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] and (new_i, new_j) not in visited:
            ans.append((x, y))
            arr = dfs(new_i, new_j, visited, grid)
            for a, b in arr:
                ans.append((a + x, b + y))

    return ans


def count_distinct_islands(grid) -> int:
    """
    Time Complexity: O(n*m) + log(n*m)
    Space Complexity: O(n*m)
    """
    n, m = len(grid), len(grid[0])

    visited, islands = set(), set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and (i, j) not in visited:
                new_island = tuple(dfs(i, j, visited, grid))
                if new_island not in islands:
                    islands.add(new_island)

    return len(islands)


print(count_distinct_islands([[1, 1, 0, 1, 1],
                              [1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1],
                              [1, 1, 0, 1, 1]]))
