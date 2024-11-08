def dfs(i, stack, visited, adj):
    visited[i] = True

    for adj_node, w in adj[i]:
        if not visited[adj_node]:
            dfs(adj_node, stack, visited, adj)

    stack.append(i)


def shortest_path(n, edges):
    """
    !! Only for DAG !!

    Time Complexity: O(n+e)
    Space Complexity: O(n)
    """
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))

    visited = [False] * n

    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(i, stack, visited, adj)

    ans = [float('inf')] * n
    ans[0] = 0

    while stack:
        node = stack.pop()
        for adj_node, w in adj[node]:
            ans[adj_node] = min(ans[adj_node], w + ans[node])

    return ans


print(shortest_path(4, [[0, 1, 2], [0, 2, 1]]))
