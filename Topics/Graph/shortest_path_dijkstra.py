import heapq


def shortest_path_dijkstra(n, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    start, end = 1, n

    min_heap = []
    dist = [float('inf')] * (n + 1)
    parent = [i for i in range(n + 1)]

    dist[start] = 0
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)

        for neighbor, weight in adj[curr_node]:
            if curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight

                parent[neighbor] = curr_node
                heapq.heappush(min_heap, (curr_dist + weight, neighbor))

    if dist[end] != float('inf'):
        ans, i = [], end
        while parent[i] != i:
            ans.append(i)
            i = parent[i]

        ans.append(i)
        return [dist[end]] + ans[::-1]

    return -1


print(shortest_path_dijkstra(5, [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]))
