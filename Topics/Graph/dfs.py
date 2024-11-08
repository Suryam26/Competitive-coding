def dfs_of_graph(adj):
    """
    Time Complexity: O(N+2E)
    Space Complexity: O(N)
    """
    dfs = []
    visited = set()

    def traverse(i):
        if i in visited:
            return

        visited.add(i)
        dfs.append(i)

        neighbour = adj[i]
        for j in neighbour:
            traverse(j)

    traverse(0)
    return dfs


adjMatrix = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(dfs_of_graph(adjMatrix))
