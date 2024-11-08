def shortest_path(adj, src):
    """
    Time Complexity: O(N+2E)
    Space Complexity: O(N)
    """
    n = len(adj)

    ans = [float('inf')] * n
    ans[src] = 0

    queue = [src]
    while queue:
        node = queue.pop(0)

        for adj_node in adj[node]:
            if ans[adj_node] > 1 + ans[node]:
                ans[adj_node] = 1 + ans[node]
                queue.append(adj_node)

    return ans
