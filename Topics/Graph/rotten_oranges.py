def oranges_rotting(grid) -> int:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    """
    n, m = len(grid), len(grid[0])
    move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    queue, visited = [], set()

    total = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                total += 1

            if grid[i][j] == 2:
                queue.append((i, j))

    if not total:
        return 0

    time = 0
    while queue:
        for _ in range(len(queue)):
            i, j = queue.pop(0)

            for x, y in move:
                x, y = i + x, j + y
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 1 and (x, y) not in visited:
                    queue.append((x, y))
                    visited.add((x, y))

        time += 1

    return time - 1 if total == len(visited) else -1


print(oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
