def dfs(i, j, image, color, new_color, visited):
    n, m = len(image), len(image[0])

    if i < 0 or i >= n or j < 0 or j >= m:
        return

    if image[i][j] != color or (i, j) in visited:
        return

    visited.add((i, j))
    image[i][j] = new_color

    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for x, y in move:
        dfs(i + x, j + y, image, color, new_color, visited)


def flood_fill(image, sr, sc, new_color):
    """
    Time Complexity: O(n*m)
    Space Complexity: O(n*m)
    """
    visited = set()
    init_color = image[sr][sc]
    dfs(sr, sc, image, init_color, new_color, visited)
    return image
