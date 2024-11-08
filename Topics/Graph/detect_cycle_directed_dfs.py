def detect_cycle(i, visited, path_visited, adj):
    visited[i] = True
    path_visited[i] = True

    for adj_node in adj[i]:
        if not visited[adj_node] and detect_cycle(adj_node, visited, path_visited, adj):
            return True

        elif path_visited[adj_node]:
            return True

    path_visited[i] = False
    return False


def check_cycle(adj):
    """
    Time Complexity: O(n+e)
    Space Complexity: O(n)
    """
    n = len(adj)

    visited = [False] * n
    path_visited = [False] * n

    for i in range(n):
        if not visited[i] and detect_cycle(i, visited, path_visited, adj):
            return True

    return False


print(check_cycle([[], [2], [3], [4, 7], [5], [6], [], [5], [9], [10], [8]]))
