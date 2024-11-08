def bfs(i, colour, colours, adj_matrix):
    queue = [(i, colour)]

    while queue:
        node, curr_col = queue.pop(0)

        for adjacent_node in adj_matrix[node]:
            if colours[adjacent_node] == -1:
                colours[adjacent_node] = not curr_col
                queue.append((adjacent_node, not curr_col))

            elif colours[adjacent_node] == curr_col:
                return False

    return True


def check_bipartite(adj_matrix):
    """
    Time Complexity: O(n+2e)
    Space Complexity: O(n)
    """
    n = len(adj_matrix)

    colours = [-1] * n
    for i in range(n):
        if colours[i] == -1 and not bfs(i, True, colours, adj_matrix):
            return False

    return True


print(check_bipartite([[2, 3], [], [3], [1]]))
