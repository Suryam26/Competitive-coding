import heapq


def minimum_multiplications(arr, start, end):
    mod = 100000
    min_heap = []
    dist = [float('inf')] * mod

    dist[start] = 0
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        steps, node = heapq.heappop(min_heap)

        if node == end:
            return steps

        for num in arr:
            prod = (num * node) % mod
            if steps + 1 < dist[prod]:
                dist[prod] = steps + 1
                heapq.heappush(min_heap, (steps + 1, prod))
    return -1
