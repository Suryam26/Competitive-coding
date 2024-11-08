def topological_sort(adj):
    n = len(adj)

    in_degree = [0] * n
    for node in adj:
        for adj_node in node:
            in_degree[adj_node] += 1

    queue = []
    for node in range(n):
        if not in_degree[node]:
            queue.append(node)

    topological = []
    while queue:
        node = queue.pop(0)
        topological.append(node)

        for adj_node in adj[node]:
            in_degree[adj_node] -= 1
            if not in_degree[adj_node]:
                queue.append(adj_node)

    return topological


print(topological_sort([[], [], [3], [1], [0, 1], [0, 2]]))
