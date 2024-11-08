from disjoint_set import DisjointSet


def largest_island(grid):
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    n = len(grid)

    ds = DisjointSet(n * n)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                for x, y in move:
                    new_x, new_y = i + x, j + y
                    if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        cell, new_cell = i * n + j, new_x * n + new_y
                        if ds.find_parent(cell) != ds.find_parent(new_cell):
                            ds.union_by_size(cell, new_cell)

    ans = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                visited = set()

                for x, y in move:
                    new_x, new_y = i + x, j + y
                    if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        new_cell = new_x * n + new_y
                        parent = ds.find_parent(new_cell)
                        if parent not in visited:
                            visited.add(parent)

                curr_size = 1
                for parent in visited:
                    curr_size += ds.size[parent]

                ans = max(ans, curr_size)

    for i in range(n * n):
        parent = ds.find_parent(i)
        ans = max(ans, ds.size[parent])

    return ans
