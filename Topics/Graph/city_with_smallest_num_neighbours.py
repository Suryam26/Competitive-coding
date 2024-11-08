import heapq


def dijkstra(graph, start):
    min_heap = []
    distances = [float('inf')] * len(graph)

    distances[start] = 0
    heapq.heappush(min_heap, (0, start))

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        for neighbour, weight in graph[node]:
            if dist + weight < distances[neighbour]:
                distances[neighbour] = dist + weight
                heapq.heappush(min_heap, (dist + weight, neighbour))

    return distances


def find_city(n, edges, distance_threshold):
    adj_matrix = [[] for _ in range(n)]
    for u, v, w in edges:
        adj_matrix[u].append((v, w))
        adj_matrix[v].append((u, w))

    ans = []
    for i in range(n):
        ans.append(dijkstra(adj_matrix, i))

    count, city = n + 1, -1
    for i in range(n):
        curr_count = 0
        for j in range(n):
            if ans[i][j] <= distance_threshold:
                curr_count += 1

        if curr_count <= count:
            count = curr_count
            city = i

    return city
