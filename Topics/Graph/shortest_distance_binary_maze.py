def shortest_path(grid, source, destination):
    n, m = len(grid), len(grid[0])

    sx, sy = source
    dx, dy = destination

    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    dist = [[float('inf') for _ in range(m)] for _ in range(n)]
    dist[sx][sy] = 0

    queue = [(0, sx, sy)]
    while queue:
        w, x, y = queue.pop(0)

        for i, j in moves:
            xi, yj = x + i, y + j
            if 0 <= xi < n and 0 <= yj < m and grid[xi][yj] == 1 and w + 1 < dist[xi][yj]:
                dist[xi][yj] = w + 1
                queue.append((dist[xi][yj], xi, yj))

    if dist[dx][dy] == float('inf'):
        return -1

    return dist[dx][dy]
