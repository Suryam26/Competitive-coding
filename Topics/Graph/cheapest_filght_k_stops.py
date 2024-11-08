def cheapest_flight(n, flights, src, dst, k):
    adj = [[] for _ in range(n)]
    for u, v, price in flights:
        adj[u].append((v, price))

    dist = [float('inf')] * n
    dist[src] = 0

    queue = [(0, src, 0)]
    while queue:
        stops, node, prev_price = queue.pop(0)

        if stops <= k:
            for neighbour, price in adj[node]:
                if prev_price + price < dist[neighbour]:
                    dist[neighbour] = prev_price + price
                    queue.append((stops + 1, neighbour, dist[neighbour]))

    if dist[dst] == float('inf'):
        return -1

    return dist[dst]
