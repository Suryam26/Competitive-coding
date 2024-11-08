def bellman_ford(edges, start):
    """
    Time Complexity: O(E^2)
    Space Complexity: O(V)
    """
    n = len(edges)

    distances = [float("inf")] * n
    distances[start] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Check for negative cycle
    for u, v, w in edges:
        if distances[u] + w < distances[v]:
            return -1

    return distances
