import heapq


def count_paths(n, roads):
    mod = 10 ** 9 + 7
    graph = [[] for _ in range(n)]
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))

    min_heap = []
    distances = [float('inf')] * n
    ways = [0] * n

    distances[0] = 0
    ways[0] = 1
    heapq.heappush(min_heap, (0, 0))

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        for neighbor, weight in graph[node]:
            if distances[neighbor] > dist + weight:
                distances[neighbor] = dist + weight
                ways[neighbor] = ways[node]
                heapq.heappush(min_heap, (distances[neighbor], neighbor))

            elif dist + weight == distances[neighbor]:
                ways[neighbor] = (ways[neighbor] + ways[node]) % mod

    return ways[n - 1]
