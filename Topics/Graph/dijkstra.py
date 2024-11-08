import heapq


def dijkstra(graph, start):
    """
    Computes the shortest path from start to all other nodes in the graph.
    Time Complexity: O(E * (log V))
    Space Complexity: O(V)
    """
    min_heap = []
    distances = [float('inf')] * len(graph)

    distances[start] = 0
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        for neighbor, weight in graph[node]:
            if dist + weight < distances[neighbor]:
                distances[neighbor] = dist + weight
                heapq.heappush(min_heap, (dist + weight, neighbor))

    return distances
