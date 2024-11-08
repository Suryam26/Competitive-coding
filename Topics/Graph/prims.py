import heapq


def prims(graph):
    mst = []

    min_heap = []
    visited = [False] * len(graph)

    min_heap.append((0, 0, -1))

    min_sum = 0
    while min_heap:
        w, node, parent = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True
        min_sum += w
        mst.append((node, parent))

        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (weight, neighbor, node))

    return min_sum
