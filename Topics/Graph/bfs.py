def bfs_of_graph(adj):
    """
    Time Complexity: O(N+2E)
    Space Complexity: O(N)
    """
    bfs = []

    if not adj:
        return []

    queue = [0]
    visited = {0}
    while queue:
        n = queue.pop(0)

        bfs.append(n)

        for i in adj[n]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

    return bfs


adjMatrix = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(bfs_of_graph(adjMatrix))
