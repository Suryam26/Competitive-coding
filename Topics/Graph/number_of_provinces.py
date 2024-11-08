def dfs(i, adj, visited, n):
    if i in visited:
        return

    visited.add(i)
    for j in range(n):
        if adj[i][j] == 1:
            dfs(j, adj, visited, n)


def num_provinces(adj):
    """
    Time Complexity: O(N) + O(N+2E) ~ O(N)
    """
    n = len(adj)

    ans, visited = 0, set()
    for i in range(n):
        if i not in visited:
            ans += 1
            dfs(i, adj, visited, n)

    return ans
