def dfs(i, color, colors, adj):
    colors[i] = color

    for adj_node in adj[i]:
        if colors[adj_node] == -1 and not dfs(adj_node, not color, colors, adj):
            return False

        elif colors[i] == color:
            return False

    return True


def check_bipartite(adj):
    n = len(adj)
    colors = [-1] * n

    for i in range(n):
        if colors[i] == -1:
            if not dfs(i, True, colors, adj):
                return False

    return True


print(check_bipartite([[2, 3], [], [3], [1]]))
