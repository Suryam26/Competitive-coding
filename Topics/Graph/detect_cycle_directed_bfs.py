def khans_algo(adj):
    n = len(adj)

    in_degree = [0] * n
    for node in adj:
        for adj_node in node:
            in_degree[adj_node] += 1

    queue = []
    for node in range(n):
        if in_degree[node] == 0:
            queue.append(node)

    count = 0
    while queue:
        node = queue.pop(0)
        count += 1

        for adj_node in adj[node]:
            in_degree[adj_node] -= 1
            if in_degree[adj_node] == 0:
                queue.append(adj_node)

    return count != n


print(khans_algo([[], [2], [3], [4, 7], [5], [6], [], [5], [9], [10], [8]]))
