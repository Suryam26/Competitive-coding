def topological_sort_util(i, visited, stack, adj):
    visited[i] = True

    for adj_node in adj[i]:
        if not visited[adj_node]:
            topological_sort_util(adj_node, visited, stack, adj)

    stack.append(i)


def topological_sort(adj):
    n = len(adj)

    visited = [False] * n
    stack = []

    for i in range(n):
        if not visited[i]:
            topological_sort_util(i, visited, stack, adj)

    return stack[::-1]


print(topological_sort([[], [], [3], [1], [0, 1], [0, 2]]))
