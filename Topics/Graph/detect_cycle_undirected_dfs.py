def dfs(node, parent, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(neighbor, node, graph, visited):
                return True
        elif neighbor != parent:
            return True

    return False


def detect_cycle(graph):
    """
    Time Complexity: O(N+2E)
    Space Complexity: O(N)
    """
    n = len(graph)

    visited = set()
    for i in range(n):
        if i not in visited and dfs(i, -1, graph, visited):
            return True

    return False


print(detect_cycle([[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]))
print(detect_cycle([[], [2], [1, 3], [2]]))
