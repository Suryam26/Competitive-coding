def is_possible(n, prerequisites):
    adj = [[] for _ in range(n)]
    for u, v in prerequisites:
        adj[v].append(u)

    in_degree = [0] * n
    for node in adj:
        for adj_node in node:
            in_degree[adj_node] += 1

    queue = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    count = 0
    while queue:
        node = queue.pop(0)
        count += 1

        for adj_node in adj[node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                queue.append(adj_node)

    return count == n


print(is_possible(4, [[1, 0], [2, 1], [3, 2]]))
