def oranges_rotting(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    time, oranges, count = 0, 0, 0
    queue = []

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                oranges += 1

            if grid[i][j] == 2:
                queue.append((i, j))

    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        k = len(queue)
        count += k

        while k:
            rotten = queue.pop(0)

            x, y = rotten[0], rotten[1]
            for i in dxy:
                nx = x + i[0]
                ny = y + i[1]

                if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                    continue

                grid[nx][ny] = 2
                queue.append((nx, ny))

            k -= 1
        if queue:
            time += 1

    return time if oranges == count else -1


orange_grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(oranges_rotting(orange_grid))
