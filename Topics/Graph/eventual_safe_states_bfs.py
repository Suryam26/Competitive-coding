def eventual_safe_nodes(n, adj):
    new_adj = [[] for _ in range(n)]

    in_degree = [0] * n
    for i in range(n):
        in_degree[i] = 0
        for adj_node in adj[i]:
            new_adj[adj_node].append(i)
            in_degree[i] += 1

    queue = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    ans = []
    while queue:
        node = queue.pop(0)
        ans.append(node)

        for adj_node in new_adj[node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                queue.append(adj_node)

    return sorted(ans)
