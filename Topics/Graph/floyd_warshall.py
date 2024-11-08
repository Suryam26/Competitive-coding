def floyd_warshall(matrix):
    """
    Time Complexity: O(V^3)
    Space Complexity: O(V^2)
    """
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            elif matrix[i][j] == -1:
                matrix[i][j] = float("inf")

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    # Check for negative cycle
    for i in range(n):
        if matrix[i][i] < 0:
            return -1

    return matrix
