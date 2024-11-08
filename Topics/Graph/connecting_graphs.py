from disjoint_set import DisjointSet


def connecting_graphs(n, edges):
    m = len(edges)

    if m < n - 1:
        return -1

    ds = DisjointSet(n)

    for u, v in edges:
        ds.union_by_size(u, v)

    ans = 0
    for i in range(n):
        if ds.find_parent(i) == i:
            ans += 1

    return ans - 1
