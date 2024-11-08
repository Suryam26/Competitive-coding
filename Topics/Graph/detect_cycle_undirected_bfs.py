def bfs(i, graph, visited):
    queue = [(i, -1)]
    visited.add(i)

    while queue:
        node, parent = queue.pop(0)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, node))
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
        if i not in visited and bfs(i, graph, visited):
            return True

    return False


print(detect_cycle([[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]))
print(detect_cycle([[], [2], [1, 3], [2]]))
