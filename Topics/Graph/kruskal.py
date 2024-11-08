from disjoint_set import DisjointSet


def kruskal(n, edges):
    """
    Time Complexity: O(E logE) + O(4Alpha) ~ O(E logE)
    Space Complexity: O(N + E)
    """
    mst = []
    edges.sort(key=lambda x: (x[2], x[0], x[1]))

    ds = DisjointSet(n)

    min_sum = 0
    for u, v, w in edges:
        if ds.find_parent(u) != ds.find_parent(v):
            ds.union_by_size(u, v)
            mst.append((u, v))
            min_sum += w

    return min_sum


print(kruskal(3, [(0, 1, 5), (1, 2, 3), (0, 2, 1)]))
