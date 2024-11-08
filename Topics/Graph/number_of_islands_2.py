from disjoint_set import DisjointSet


def number_of_islands(n, m, operators):
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    ds = DisjointSet(n * m)
    visited = [[False for _ in range(m)] for _ in range(n)]

    ans, curr_count = [], 0
    for x, y in operators:
        if not visited[x][y]:
            curr_count += 1
            visited[x][y] = True

            for i, j in move:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < n and 0 <= new_y < m and visited[new_x][new_y]:
                    cell, new_cell = (x * m) + y, (new_x * m) + new_y
                    if ds.find_parent(cell) != ds.find_parent(new_cell):
                        curr_count -= 1
                        ds.union_by_size(cell, new_cell)

        ans.append(curr_count)

    return ans
