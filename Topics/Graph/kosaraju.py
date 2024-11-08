def dfs(node, visited, stack, adj):
    visited[node] = True

    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, stack, adj)

    stack.append(node)


def count_dfs(node, visited, adj):
    visited[node] = True

    for neighbor in adj[node]:
        if not visited[neighbor]:
            count_dfs(neighbor, visited, adj)


def cal_scc(adj):
    """
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    n = len(adj)

    stack = []
    visited = [False] * n

    # Sorting the vertices according to finish-time
    for node in range(n):
        if not visited[node]:
            dfs(node, visited, stack, adj)

    # Reversing all the edges in the graph
    reverse = [[] for _ in range(n)]
    for node in range(n):
        visited[node] = False
        for neighbor in adj[node]:
            reverse[neighbor].append(node)

    # Counting SSC using DFS
    ssc = 0
    while stack:
        node = stack.pop(-1)
        if not visited[node]:
            ssc += 1
            count_dfs(node, visited, reverse)

    return ssc
