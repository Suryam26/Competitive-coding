import heapq


def minimum_effort(rows, columns, heights):
    min_heap = []

    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    diff = [[float('inf') for _ in range(columns)] for _ in range(rows)]
    diff[0][0] = 0

    heapq.heappush(min_heap, (0, 0, 0))
    while min_heap:
        effort, x, y = heapq.heappop(min_heap)

        val = heights[x][y]
        for i, j in moves:
            xi, yj = x + i, y + j
            if 0 <= xi < rows and 0 <= yj < columns and max(effort, abs(val - heights[xi][yj])) < diff[xi][yj]:
                diff[xi][yj] = max(effort, abs(val - heights[xi][yj]))
                heapq.heappush(min_heap, (diff[xi][yj], xi, yj))

    return diff[rows - 1][columns - 1]
