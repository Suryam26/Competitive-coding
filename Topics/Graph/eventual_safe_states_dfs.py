def dfs(i, is_safe, path, visited, adj):
    visited[i] = True
    path[i] = True

    for adj_node in adj[i]:
        if not visited[adj_node] and dfs(adj_node, is_safe, path, visited, adj):
            return True

        elif path[adj_node]:
            return True

    is_safe[i] = True
    path[i] = False

    return False


def eventual_safe_nodes(adj):
    """
    Time Complexity: O(n+e)
    Space Complexity: O(n)
    """
    n = len(adj)

    visited = [False] * n
    path = [False] * n

    is_safe = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, is_safe, path, visited, adj)

    ans = []
    for node in range(n):
        if is_safe[node]:
            ans.append(node)

    return ans
